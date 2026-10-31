# 🛠️ Guia de Integração das Ferramentas & Migração para Linux (Ubuntu 24.04)

> Este documento preserva o contexto arquitetural de como as novas ferramentas adicionadas ao **Awesome AI & Open Source Arsenal** podem ser diretamente integradas para turbinar o pipeline do projeto **ReposIA**, além do guia prático de migração do ecossistema macOS para Linux.

---

## 🎯 1. Como as Novas Ferramentas Ajudam o ReposIA no Linux

### 1.1 🔍 [Upscayl](https://github.com/upscayl/upscayl) — Super-resolução para OCR em Carrosséis
* **Problema atual**: Carrosséis do Instagram salvam imagens com compressão JPEG e textos com fontes pequenas ou estilizadas. No Linux, o OCR pode perder letras em slides de baixa resolução.
* **Aplicação no ReposIA**:
  - No Linux, o Upscayl disponibiliza binários CLI (`upscayl-bin` via Vulkan/NCNN).
  - Pode ser chamado antes do OCR para ampliar em 4x a nitidez de slides granulados salvos em `scratch/slides_images/`.
  - **Comando de instalação no Ubuntu**: Baixar AppImage ou pacote Flatpak (`flatpak install flathub org.upscayl.Upscayl`) ou compilar o CLI via Vulkan.

### 1.2 🤖 [OpenCode](https://github.com/anomalyco/opencode) & [Orca](https://github.com/stablyai/orca) — Automação e Orquestração Autônoma
* **Problema atual**: A execução do pipeline depende de disparos manuais ou do agente no VS Code.
* **Aplicação no ReposIA**:
  - O **OpenCode** opera no terminal Linux nativamente (`npx opencode` ou instalação global). Pode rodar em um cron job diário para verificar se há novos posts, executar o scraper, tratar exceções de DOM e rodar `audit_repos.py`.
  - O **Orca** permite orquestrar agentes em frotas isoladas por `git worktree`. Um agente pode varrer o Instagram enquanto outro atualiza métricas e resolve conflitos no README.

### 1.3 🛡️ [Security Audit Skill](https://github.com/cloudflare/security-audit-skill) — Auditoria de Segurança dos Scripts
* **Problema atual**: O pipeline executa automações de navegador, scripts Python com subprocessos e lida com tokens da GitHub API (`gh auth token`).
* **Aplicação no ReposIA**:
  - Skill oficial da Cloudflare plugada em coding agents (Claude Code, Antigravity, OpenCode).
  - Executa verificações automatizadas de injeção de comandos, sanitização de dados extraídos via OCR e impede vazamento acidental de tokens em logs de auditoria.

### 1.4 🧠 [Janas](https://github.com/prabanta-dev/janas) — Classificação Inteligente 100% Offline
* **Problema atual**: Quando novos repositórios são encontrados pelo OCR, suas descrições originais do GitHub estão em inglês e precisam de tradução, refinamento e escolha da categoria (1 a 13).
* **Aplicação no ReposIA**:
  - Motor em C puro, compila com `gcc -O3` ou `clang` no Ubuntu 24.04.
  - Executa modelos abertos (ex: Qwen, Llama 3) com consumo mínimo de RAM e até 13x mais rápido que `llama.cpp`.
  - Um script Python local pode chamar o binário do Janas para ler o README do repositório recém-descoberto e retornar o JSON pronto com categoria e descrição polida em português.

### 1.5 💻 [Pake](https://github.com/tw93/Pake) — Aplicativo Desktop Nativo do Arsenal
* **Problema atual**: O catálogo é consumido primariamente via Markdown no GitHub.
* **Aplicação no ReposIA**:
  - Baseado em Rust e Tauri.
  - Gera em 1 comando um aplicativo desktop nativo para Linux (`.deb` / `.AppImage`, <15 MB):
    ```bash
    pake https://github.com/rogerioc/awesome-ai-arsenal --name "Arsenal"
    ```

---

## 🐧 2. Adaptação do Pipeline do macOS para Linux

No Linux (Ubuntu 24.04), dois componentes específicos do macOS precisam ser substituídos:

### 2.1 OCR (Apple Vision Framework -> Tesseract / EasyOCR)
* **No macOS**: O projeto usava `scripts/ocr.swift` compilado com `swiftc` chamando `VNRecognizeTextRequest`.
* **No Linux**: Instalar o **Tesseract OCR**:
  ```bash
  sudo apt update
  sudo apt install -y tesseract-ocr tesseract-ocr-por tesseract-ocr-eng
  pip install pytesseract
  ```
* **Adapter Python (`scripts/ocr_linux.py`)**:
  ```python
  import sys
  import pytesseract
  from PIL import Image

  for img_path in sys.argv[1:]:
      try:
          text = pytesseract.image_to_string(Image.open(img_path), lang="por+eng")
          print(f"--- FILE: {img_path} ---")
          print(text)
      except Exception as e:
          pass
  ```

### 2.2 Scraper do Navegador (AppleScript -> Playwright)
* **No macOS**: O script controlava o Brave via `osascript` (AppleScript).
* **No Linux**: Usar **Playwright** com o Brave Browser instalado ou Chromium headless:
  ```bash
  pip install playwright
  playwright install chromium
  ```
  O Playwright roda nativamente em servidores Linux (mesmo sem monitor / headless) com performance e estabilidade superiores ao AppleScript.

---

## 📂 3. Estrutura dos Dados e Diretórios

* `data/repos_catalog.json`: Base principal com todas as 242 ferramentas cadastradas.
* `data/saved_posts.json`: Lista de todos os posts salvos já processados (evita reprocessamento).
* `data/repos_audit.json`: Relatório de saúde gerado pela API do GitHub.
* `scripts/audit_repos.py`: Auditor paralelo multiplataforma (funciona identicamente no Linux).
* `scripts/update_arsenal.py`: Script central de orquestração.
* `scripts/ocr_linux.py`: Utilitário de OCR ultraleve baseado em Tesseract para Linux.

---

## 🔮 4. Roadmap & Melhorias Futuras

### 4.1 🏷️ Classificação Inteligente Automática (LLM / API)
* **Objetivo:** Substituir a categorização manual ou por palavras-chave por inferência de LLM que lê o README/descrição do repositório recém-descoberto e classifica diretamente em uma das 13 categorias oficiais, gerando a descrição concisa em português.
* **Opções Arquiteturais Avaliadas:**
  1. **Nuvem (Zero RAM / Recomendada):** Chamada via Gemini API (cota gratuita) ou Groq API — resposta em <1s sem onerar a CPU nem a memória RAM local.
  2. **Local Leve (Ollama):** Uso do modelo `deepseek-r1:1.5b` (1.1 GB) já instalado no ambiente local, consumindo o mínimo de memória e rodando na CPU i5.
  3. **Janas / C Engine:** Binário C puro compilado no Linux rodando quantizações GGUF ultra-otimizadas.
