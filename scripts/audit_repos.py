#!/usr/bin/env python3
"""
audit_repos.py - Auditor de Saúde, Atividade e Tempo de Inatividade dos Repositórios

Funcionalidades:
1. Consulta a API oficial do GitHub em paralelo (alta velocidade com ThreadPoolExecutor).
2. Usa autenticação automática via `gh auth token` (evitando limites de rate-limit).
3. Calcula o tempo exato (em anos e dias) desde o último commit / push.
4. Destaca e marca repositórios com regras claras:
   - 🚨 [CRÍTICO: +5 ANOS SEM UPDATE] -> Marcado com alerta vermelho de alta defasagem.
   - ⚠️ [DEFASADO: +2 ANOS SEM UPDATE] -> Projetos legados/estáticos.
   - 📦 [ARQUIVADO NO GITHUB] -> Repositórios em modo somente-leitura.
   - ❌ [ERRO / 404] -> Repositórios que foram deletados ou renomeados.
   - 🟢 [ATIVO / ATUALIZADO] -> Commits recentes (< 1 ano).
5. Salva o relatório consolidado em `data/repos_audit.json`.

Uso:
  python3 scripts/audit_repos.py
  python3 scripts/audit_repos.py --outdated-only
  python3 scripts/audit_repos.py --five-years-only
"""

import os
import sys
import json
import time
import argparse
import subprocess
import urllib.request
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
CATALOG_FILE = os.path.join(DATA_DIR, "repos_catalog.json")
AUDIT_OUTPUT_FILE = os.path.join(DATA_DIR, "repos_audit.json")

def get_github_headers():
    gh_token = subprocess.run(["/usr/local/bin/gh", "auth", "token"], capture_output=True, text=True).stdout.strip()
    headers = {
        "User-Agent": "Awesome-Arsenal-Auditor",
        "Accept": "application/vnd.github.v3+json"
    }
    if gh_token:
        headers["Authorization"] = f"token {gh_token}"
    return headers

def check_one_repo(item, headers):
    name = item.get("name", "")
    repo_id = item.get("repo_id", "")
    url = f"https://api.github.com/repos/{repo_id}"
    req = urllib.request.Request(url, headers=headers)
    
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            pushed_at = data.get("pushed_at")
            is_archived = data.get("archived", False)
            stars = data.get("stargazers_count", 0)
            forks = data.get("forks_count", 0)
            license_name = data.get("license", {}).get("spdx_id") if data.get("license") else None
            
            years = 0.0
            days = 0
            if pushed_at:
                dt = datetime.strptime(pushed_at, "%Y-%m-%dT%H:%M:%SZ")
                days = (datetime.utcnow() - dt).days
                years = round(days / 365.25, 2)
                
            return {
                "name": name,
                "repo_id": repo_id,
                "category": item.get("category", ""),
                "stars": stars,
                "forks": forks,
                "archived": is_archived,
                "pushed_at": pushed_at,
                "years_inactive": years,
                "days_inactive": days,
                "license": license_name,
                "status": "OK"
            }
    except urllib.error.HTTPError as e:
        return {"name": name, "repo_id": repo_id, "status": f"HTTP_{e.code}"}
    except Exception as e:
        return {"name": name, "repo_id": repo_id, "status": f"ERROR_{str(e)}"}

def main():
    parser = argparse.ArgumentParser(description="Audita atividade e tempo de inatividade dos repositórios.")
    parser.add_argument("--outdated-only", action="store_true", help="Exibe apenas repositórios defasados, arquivados ou com erro.")
    parser.add_argument("--five-years-only", action="store_true", help="Filtra exclusivamente repositórios com mais de 5 anos sem commits.")
    args = parser.parse_args()

    if not os.path.exists(CATALOG_FILE):
        print(f"❌ Catálogo não encontrado em {CATALOG_FILE}")
        sys.exit(1)

    with open(CATALOG_FILE, "r", encoding="utf-8") as f:
        catalog = json.load(f)

    headers = get_github_headers()
    print(f"🔍 Auditando {len(catalog)} repositórios em paralelo via GitHub API...")
    
    start_time = time.time()
    with ThreadPoolExecutor(max_workers=16) as executor:
        results = list(executor.map(lambda it: check_one_repo(it, headers), catalog))
    
    elapsed = round(time.time() - start_time, 2)
    print(f"⚡ Auditoria concluída em {elapsed}s!\n")

    # Classificação por faixa de tempo
    outdated_5y = []
    outdated_2y = []
    outdated_1y = []
    healthy = []
    archived = []
    errors = []

    for r in results:
        status = r.get("status")
        if status != "OK":
            errors.append(r)
            continue
            
        if r.get("archived"):
            archived.append(r)
            continue
            
        years = r.get("years_inactive", 0)
        if years >= 5.0:
            outdated_5y.append(r)
        elif years >= 2.0:
            outdated_2y.append(r)
        elif years >= 1.0:
            outdated_1y.append(r)
        else:
            healthy.append(r)

    # Exibição
    print("=" * 65)
    print(f"📊 RELATÓRIO DE SAÚDE & ATIVIDADE ({len(catalog)} REPOSITÓRIOS)")
    print("=" * 65)
    print(f"  🟢 Ativos (<1 ano sem push):         {len(healthy):>3} ({round(len(healthy)/len(catalog)*100, 1)}%)")
    print(f"  🟡 Estáveis (1 a 2 anos):             {len(outdated_1y):>3} ({round(len(outdated_1y)/len(catalog)*100, 1)}%)")
    print(f"  ⚠️ Defasados (2 a 5 anos):           {len(outdated_2y):>3} ({round(len(outdated_2y)/len(catalog)*100, 1)}%)")
    print(f"  🚨 CRÍTICOS (+5 ANOS SEM UPDATE):    {len(outdated_5y):>3} ({round(len(outdated_5y)/len(catalog)*100, 1)}%)")
    print(f"  📦 Arquivados no GitHub:             {len(archived):>3} ({round(len(archived)/len(catalog)*100, 1)}%)")
    print(f"  ❌ Erros / 404 (Deletados):          {len(errors):>3} ({round(len(errors)/len(catalog)*100, 1)}%)")
    print("=" * 65)

    if outdated_5y:
        print("\n🚨 REPOSITÓRIOS COM MAIS DE 5 ANOS SEM UPDATE (MARCADOS):")
        for o in sorted(outdated_5y, key=lambda x: x["years_inactive"], reverse=True):
            n = o["name"]
            r = o["repo_id"]
            y = o["years_inactive"]
            d = o.get("pushed_at", "")[:10]
            st = o.get("stars", 0)
            print(f"  • [🚨 +{y} ANOS] {n} ({r}) - {st:,} ⭐ | Último commit em: {d}")

    if not args.five_years_only:
        if archived:
            print("\n📦 REPOSITÓRIOS ARQUIVADOS OFICIALMENTE NO GITHUB:")
            for a in archived:
                n = a["name"]
                r = a["repo_id"]
                d = a.get("pushed_at", "")[:10]
                st = a.get("stars", 0)
                print(f"  • [📦 ARQUIVADO] {n} ({r}) - {st:,} ⭐ | Último push: {d}")

        if outdated_2y and not args.outdated_only:
            print("\n⚠️ REPOSITÓRIOS COM 2 A 5 ANOS SEM COMMITS:")
            for o in sorted(outdated_2y, key=lambda x: x["years_inactive"], reverse=True):
                n = o["name"]
                r = o["repo_id"]
                y = o["years_inactive"]
                d = o.get("pushed_at", "")[:10]
                print(f"  • [⚠️ {y} anos] {n} ({r}) - Último push: {d}")

        if errors:
            print("\n❌ REPOSITÓRIOS NÃO ENCONTRADOS (404 OU DELETADOS):")
            for e in errors:
                n = e["name"]
                r = e["repo_id"]
                s = e.get("status")
                print(f"  • [❌ {s}] {n} ({r})")

    # Salva relatório JSON completo
    os.makedirs(DATA_DIR, exist_ok=True)
    with open(AUDIT_OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump({
            "generated_at": datetime.utcnow().isoformat() + "Z",
            "summary": {
                "total": len(catalog),
                "healthy": len(healthy),
                "outdated_1y": len(outdated_1y),
                "outdated_2y": len(outdated_2y),
                "outdated_5y": len(outdated_5y),
                "archived": len(archived),
                "errors": len(errors)
            },
            "critical_5y": outdated_5y,
            "archived": archived,
            "outdated_2y": outdated_2y,
            "outdated_1y": outdated_1y,
            "healthy": healthy,
            "errors": errors
        }, f, ensure_ascii=False, indent=2)

    print(f"\n💾 Relatório de auditoria salvo em: {AUDIT_OUTPUT_FILE}")

if __name__ == "__main__":
    main()
