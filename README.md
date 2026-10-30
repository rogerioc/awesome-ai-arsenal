<div align="center">

# ⚡ Awesome AI & Open Source Arsenal

> Uma curadoria definitiva com **242 ferramentas e repositórios open-source de ponta** para IA, desenvolvimento, automação, cibersegurança e self-hosting.

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub Projects](https://img.shields.io/badge/Projetos-242-blue.svg)](#-categorias)

</div>

## 🎯 Guia Rápido por Tarefa (Quick Lookup for Agents & Devs)

> Se você é um **Desenvolvedor** ou um **Agente de IA** procurando a ferramenta ideal para resolver um problema específico, use a tabela rápida abaixo:

| O que você precisa fazer? | Ferramentas Recomendadas | Categoria Direta |
|---|---|---|
| **Rastrear e extrair dados web para LLMs sem bloqueios** | [`Crawl4AI`](https://github.com/unclecode/crawl4ai), [`Browser-Use`](https://github.com/browser-use/browser-use), [`Scrapling`](https://github.com/D4Vinci/Scrapling), [`Camofox`](https://github.com/jo-inc/camofox-browser), [`PinchTab`](https://github.com/pinchtab/pinchtab) | [4. 🌐 Automação & Scraping](#categoria-4) |
| **Executar LLMs locais & otimizar custo de tokens** | [`Ollama`](https://github.com/ollama/ollama), [`vLLM`](https://github.com/vllm-project/vllm), [`Janas`](https://github.com/prabanta-dev/janas), [`DSPy`](https://github.com/stanfordnlp/dspy), [`Awesome Token Optimization`](https://github.com/pleasedodisturb/awesome-llm-token-optimization) | [2. 🧠 LLMs & Inferência](#categoria-2) |
| **Visão computacional, detecção de objetos & ativos 3D** | [`Upscayl`](https://github.com/upscayl/upscayl), [`Detectron2`](https://github.com/facebookresearch/detectron2), [`TRELLIS.2`](https://github.com/microsoft/TRELLIS.2), [`Fooocus`](https://github.com/lllyasviel/Fooocus), [`LivePortrait`](https://github.com/KwaiVGI/LivePortrait), [`Diffusers`](https://github.com/huggingface/diffusers) | [3. 👁️ Visão & 3D](#categoria-3) |
| **Assistente de código, observabilidade & compressão de tokens** | [`OpenCode`](https://github.com/anomalyco/opencode), [`Aider`](https://github.com/paul-gauthier/aider), [`RTK`](https://github.com/rtk-ai/rtk), [`GitIngest`](https://github.com/coderamp-labs/gitingest), [`ccusage`](https://github.com/ccusage/ccusage), [`AgentTrace`](https://github.com/luoyuctl/agenttrace) | [1. 🤖 Agentes](#categoria-1) / [9. 💻 DevTools](#categoria-9) |
| **Agentes autônomos que operam o computador (GUI/OS)** | [`Agent-S`](https://github.com/simular-ai/Agent-S), [`Cindy`](https://github.com/makecindy/cindy), [`CLI-Anything`](https://github.com/HKUDS/CLI-Anything), [`Show-1`](https://github.com/showlab/Show-1) | [1. 🤖 Agentes de IA](#categoria-1) |
| **Automação Android, espelhamento & ecossistema mobile** | [`scrcpy`](https://github.com/Genymobile/scrcpy), [`Artemis`](https://github.com/google/artemis), [`AppAgent`](https://github.com/mnotgod96/AppAgent), [`docker-android`](https://github.com/HQarroum/docker-android), [`Termux`](https://github.com/termux/termux-app), [`LibrePods`](https://github.com/librepods-org/librepods) | [7. 📱 Mobile & Android](#categoria-7) |
| **Construir fluxos visuais, equipes multi-agente & APIs** | [`CrewAI`](https://github.com/crewAIInc/crewAI), [`Orca`](https://github.com/stablyai/orca), [`Ruflo`](https://github.com/ruvnet/ruflo), [`Dify`](https://github.com/langgenius/dify), [`OpenRig`](https://github.com/mvschwarz/openrig), [`Nango`](https://github.com/NangoHQ/nango), [`Flowise`](https://github.com/FlowiseAI/Flowise), [`n8n`](https://github.com/n8n-io/n8n) | [1. 🤖 Agentes](#categoria-1) / [10. ⚙️ DevOps](#categoria-10) |
| **Design de interfaces, diagramação visual, DER e CAD** | [`Penpot`](https://github.com/penpot/penpot), [`Excalidraw`](https://github.com/excalidraw/excalidraw), [`DrawDB`](https://github.com/drawdb-io/drawdb), [`Diagram Design`](https://github.com/cathrynlavery/diagram-design), [`Archify`](https://github.com/tt-a1i/archify) | [6. 🎨 Design & Prototipagem](#categoria-6) |
| **Substitutos self-hosted para economizar em SaaS pagos** | [`RustDesk`](https://github.com/rustdesk/rustdesk) *(TeamViewer)*, [`Jellyfin`](https://github.com/jellyfin/jellyfin) *(Plex)*, [`Joplin`](https://github.com/laurent22/joplin) *(Evernote)*, [`Spotube`](https://github.com/team-spotube/spotube) *(Spotify)*, [`Pear Desktop`](https://github.com/pear-devs/pear-desktop) *(YT Music)*, [`9Drive`](https://github.com/zenhosta/9drive) *(Google Drive)*, [`WordCraft`](https://github.com/storytold/wordcraft) *(Word)*, [`VERT`](https://github.com/VERT-sh/VERT) *(CloudConvert)*, [`LibreChat`](https://github.com/LibreChat-AI/LibreChat) *(ChatGPT)*, [`LocalSend`](https://github.com/localsend/localsend) *(AirDrop)*, [`KaraKeep`](https://github.com/karakeep-app/karakeep) *(Pocket)*, [`Supabase`](https://github.com/supabase/supabase) *(Firebase)*, [`Docmost`](https://github.com/docmost/docmost) *(Notion)* | [11. 🏠 Substitutos Open-Source](#categoria-11) |
| **Edição, clonagem de voz, download de mídias e vídeos curtos** | [`yt-dlp`](https://github.com/yt-dlp/yt-dlp), [`spotDL`](https://github.com/spotDL/spotify-downloader), [`MoneyPrinterTurbo`](https://github.com/harry0703/MoneyPrinterTurbo), [`VoxCPM`](https://github.com/OpenBMB/VoxCPM), [`Auto-Editor`](https://github.com/WyattBlue/auto-editor), [`Cobalt`](https://github.com/imputnet/cobalt), [`Whisper`](https://github.com/openai/whisper) | [5. 🎬 Áudio & Vídeo](#categoria-5) |
| **Trading quantitativo & inteligência de mercado financeiro** | [`TradingAgents`](https://github.com/TauricResearch/TradingAgents), [`OpenTerminal`](https://github.com/ErTasselli/OpenTerminal), [`Fincept Terminal`](https://github.com/Fincept-Corporation/FinceptTerminal), [`Vibe-Trading`](https://github.com/HKUDS/Vibe-Trading), [`FinRL`](https://github.com/AI4Finance-Foundation/FinRL) | [12. 📈 Negócios & Finanças](#categoria-12) |
| **Engenharia reversa, análise de vínculos OSINT e pentest** | [`Wazuh`](https://github.com/wazuh/wazuh), [`CyberChef`](https://github.com/gchq/CyberChef), [`Rea`](https://github.com/morluto/rea), [`Flowsint`](https://github.com/reconurge/flowsint), [`Wifit3`](https://github.com/derv82/wifit3), [`ESP32-BlueJammer`](https://github.com/EmenstaNougat/ESP32-BlueJammer), [`Blackbird`](https://github.com/p1ngul1n0/blackbird), [`Kali NetHunter`](https://github.com/offensive-security/kali-nethunter) | [8. 🛡️ Cibersegurança](#categoria-8) |
| **Proteger privacidade, bloquear anúncios e telemetria** | [`SearXNG`](https://github.com/searxng/searxng), [`Free-My-TV`](https://github.com/simbasjungles/free-my-tv), [`AdGuard Home`](https://github.com/AdguardTeam/AdGuardHome), [`Brave Browser`](https://github.com/brave/brave-browser), [`ExifCleaner`](https://github.com/szTheory/exifcleaner), [`uBlock Origin`](https://github.com/gorhill/uBlock) | [13. 🔒 Privacidade](#categoria-13) |

---

## 📑 Categorias

- [1. 🤖 Agentes de IA & Coding Assistants](#categoria-1)
- [2. 🧠 LLMs Locais, Fine-Tuning & Inferência](#categoria-2)
- [3. 👁️ Visão Computacional, IA Visual & 3D](#categoria-3)
- [4. 🌐 Automação de Navegador & Web Scraping](#categoria-4)
- [5. 🎬 Geração & Edição de Áudio, Vídeo e Voz](#categoria-5)
- [6. 🎨 Design, Prototipagem & Arquitetura Visual](#categoria-6)
- [7. 📱 Mobile, Android & Emulação](#categoria-7)
- [8. 🛡️ Cibersegurança, Pentest & OSINT](#categoria-8)
- [9. 💻 Ferramentas de Desenvolvimento & Terminal](#categoria-9)
- [10. ⚙️ Workflows, Orquestração & DevOps](#categoria-10)
- [11. 🏠 Substitutos Open-Source de Apps Pagos (Self-Hosted)](#categoria-11)
- [12. 📈 IA para Negócios, Marketing & Finanças](#categoria-12)
- [13. 🔒 Privacidade Digital & Anti-Rastreamento](#categoria-13)

---

<a id="categoria-1"></a>
### 1. 🤖 Agentes de IA & Coding Assistants
*Ferramentas que capacitam modelos a executar tarefas complexas, planejar ações e resolver código de forma autônoma.*

| Projeto | Repositório Oficial | Descrição |
|---|---|---|
| **500 AI Agents Projects** | [ashishpatel26/500-AI-Agents-Projects](https://github.com/ashishpatel26/500-AI-Agents-Projects) | Coleção com mais de 500 tutoriais e projetos práticos de agentes autônomos de IA. |
| **Agent-S** | [simular-ai/Agent-S](https://github.com/simular-ai/Agent-S) | Framework de agentes autônomos GUI que interagem com o sistema operacional e computadores exatamente como um ser humano. |
| **Agent-Skills** | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | Biblioteca padronizada de habilidades de engenharia prontas para produção para agentes de código (Claude Code, Cursor, Antigravity). |
| **Agentic Inbox** | [cloudflare/agentic-inbox](https://github.com/cloudflare/agentic-inbox) | Cliente de email inteligente e auto-hospedado rodando 100% em Cloudflare Workers com agente de IA integrado para triagem. |
| **AgentTrace** | [luoyuctl/agenttrace](https://github.com/luoyuctl/agenttrace) | TUI/CLI local-first em Rust para auditoria e observabilidade de sessões de agentes de código (análise de custo, tokens, latência e taxas de falha). |
| **AI Agents for Beginners** | [microsoft/ai-agents-for-beginners](https://github.com/microsoft/ai-agents-for-beginners) | Curso e guia oficial da Microsoft para criação e arquitetura de sistemas com agentes de IA. |
| **AI Memory Architecture** | [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory) | Estudos práticos e implementações de arquiteturas de memória persistente para agentes de IA. |
| **Aider** | [paul-gauthier/aider](https://github.com/paul-gauthier/aider) | Ferramenta de pair-programming de IA no terminal com suporte a git e múltiplos modelos. |
| **Anatomy** | [wheresryan22/anatomy](https://github.com/wheresryan22/anatomy) | Agent Skill especializada em gerar ilustrações isométricas interativas e detalhadas de arquiteturas complexas, diagramas de sistemas e máquinas em SVG e WebGL. |
| **Book-to-Skill** | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | Converte livros e manuais extensos em skills estruturadas e acionáveis para agentes de IA. |
| **Cindy** | [makecindy/cindy](https://github.com/makecindy/cindy) | Agente autônomo open-source pronto para uso que unifica múltiplos harnesses (Claude Code, Codex) e modelos para operar seu computador e apps locais. |
| **CLI-Anything** | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | Transforma qualquer software em CLI agent-native para permitir que agentes de IA controlem aplicações legadas e ferramentas complexas. |
| **CrewAI** | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | Framework para orquestração de equipes autônomas de agentes de IA colaborativos. |
| **Deer-Flow** | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | Framework de Deep Research e fluxos multi-agente de pesquisa profunda da ByteDance. |
| **Dify** | [langgenius/dify](https://github.com/langgenius/dify) | Plataforma de desenvolvimento de aplicações de IA e agentes com interface visual, RAG e observabilidade. |
| **Dyad** | [dyad-sh/dyad](https://github.com/dyad-sh/dyad) | Construtor local de aplicações web com IA no seu próprio computador, sem vendor lock-in. |
| **Fabric** | [danielmiessler/Fabric](https://github.com/danielmiessler/Fabric) | Framework modular open-source para potencializar a produtividade humana com IA através de prompts e padrões pré-configurados. |
| **Flowise** | [FlowiseAI/Flowise](https://github.com/FlowiseAI/Flowise) | Interface visual baseada em nós para construir e orquestrar agentes de IA e pipelines de LLM. |
| **Generative Agents** | [joonspk-research/generative_agents](https://github.com/joonspk-research/generative_agents) | Simulação computacional de comunidades de agentes autônomos (Stanford Town). |
| **Gitingest** | [cyclotruc/gitingest](https://github.com/cyclotruc/gitingest) | Converte a estrutura e código de qualquer repo GitHub em prompt otimizado para LLMs. |
| **Goose** | [aaif-goose/goose](https://github.com/aaif-goose/goose) | Agente de IA autônomo on-machine da Block para automação de tarefas complexas e execução de código. |
| **Graphify** | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | Converte qualquer codebase, documentação e schemas em um grafo de conhecimento consultável para coding agents. |
| **Langflow** | [langflow-ai/langflow](https://github.com/langflow-ai/langflow) | Interface visual baseada em nós para prototipagem e orquestração de fluxos complexos de IA e RAG. |
| **Mem0** | [mem0ai/mem0](https://github.com/mem0ai/mem0) | Camada de memória adaptativa e persistente para agentes de IA e chatbots. |
| **Mercury Agent** | [cosmicstack-labs/mercury-agent](https://github.com/cosmicstack-labs/mercury-agent) | Agente autônomo com controle granular de permissões de ferramentas, orçamentos estritos de tokens e operação contínua 24/7 com suporte a múltiplos canais (CLI, Telegram). |
| **MetaGPT** | [geekan/MetaGPT](https://github.com/geekan/MetaGPT) | Framework multi-agente que simula uma software house completa (PM, arquiteto, dev, QA). |
| **Multica** | [multica-io/multica](https://github.com/multica-io/multica) | Plataforma e ambiente para desenvolvimento de agentes de software autônomos. |
| **Open-LLM-VTuber** | [Open-LLM-VTuber/Open-LLM-VTuber](https://github.com/Open-LLM-VTuber/Open-LLM-VTuber) | Interação por voz hands-free em tempo real com qualquer LLM local integrado a avatar Live2D responsivo e interrupção natural. |
| **OpenCode** | [anomalyco/opencode](https://github.com/anomalyco/opencode) | Assistente e agente de código open-source operando diretamente no terminal, projetado para automação de tarefas de desenvolvimento, refatoração e execução paralela de comandos. |
| **OpenDots** | [CopilotKit/opendots](https://github.com/CopilotKit/opendots) | Espaço de trabalho para colegas de equipe de IA colaborativos e autônomos que operam 24/7 atendendo chamadas de voz, trocando mensagens de texto e executando ações em canais do Slack. |
| **OpenHands** | [All-Hands-AI/OpenHands](https://github.com/All-Hands-AI/OpenHands) | Plataforma open-source de agentes autônomos para desenvolvimento de software (antigo OpenDevin). |
| **OpenRig** | [mvschwarz/openrig](https://github.com/mvschwarz/openrig) | Orquestrador e rede multi-agente para Claude Code, Codex e Pi, permitindo criar equipes autônomas persistentes com papéis definidos, contexto compartilhado e execução distribuída de tarefas. |
| **Orca** | [stablyai/orca](https://github.com/stablyai/orca) | Plataforma para gerenciamento e orquestração de frotas de coding agents (Claude Code, Grok, etc.) com isolamento por worktree e suporte desktop, mobile e nuvem. |
| **Pullfrog** | [pullfrog/pullfrog](https://github.com/pullfrog/pullfrog) | Bot em GitHub Actions que analisa PRs, responde revisões e corrige falhas de CI. |
| **Ruflo** | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | Harness corporativo para enxames multi-agente com memória adaptativa contínua, inteligência auto-evolutiva e integração nativa com Claude Code e Codex. |
| **Scientific Agent Skills** | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | Biblioteca líder com mais de 170 skills e 100+ bases de dados científicas (biologia, química, medicina) para transformar agentes em pesquisadores autônomos. |
| **Superpowers** | [obra/superpowers](https://github.com/obra/superpowers) | Framework de fluxos disciplinados para coding agents (planejamento, TDD e revisão sistemática). |
| **SWE-agent** | [princeton-nlp/SWE-agent](https://github.com/princeton-nlp/SWE-agent) | Agente autônomo da Princeton que resolve bugs e issues reais no GitHub. |

---

<a id="categoria-2"></a>
### 2. 🧠 LLMs Locais, Fine-Tuning & Inferência
*Execução, otimização, RAG e especialização de modelos no seu próprio computador sem depender de nuvem.*

| Projeto | Repositório Oficial | Descrição |
|---|---|---|
| **AirLLM** | [lyogavin/airllm](https://github.com/lyogavin/airllm) | Permite executar modelos LLM gigantes (70B+) em GPUs comuns com pouca VRAM via streaming de camadas. |
| **Awesome LLM Token Optimization** | [pleasedodisturb/awesome-llm-token-optimization](https://github.com/pleasedodisturb/awesome-llm-token-optimization) | Curadoria completa de técnicas, ferramentas, compressão de contexto e estratégias para redução drástica de custos de tokens e inferência em LLMs. |
| **Colibri** | [JustVugg/colibri](https://github.com/JustVugg/colibri) | Engine em C puro para rodar modelos gigantes (744B MoE) em laptops via streaming de disco. |
| **DSPy** | [stanfordnlp/dspy](https://github.com/stanfordnlp/dspy) | Framework revolucionário para programar e otimizar pipelines de LLMs e agentes de forma determinística em vez de apenas criar prompts manuais. |
| **Janas** | [prabanta-dev/janas](https://github.com/prabanta-dev/janas) | Motor de inferência de LLMs ultrarrápido em C puro desenvolvido para executar modelos maiores que a memória RAM (como Qwen 80B em 32GB) com até 13x a velocidade do llama.cpp. |
| **Landscape of Thoughts** | [tmlr-group/landscape-of-thoughts](https://github.com/tmlr-group/landscape-of-thoughts) | Ferramenta de visualização e análise espacial do processo de raciocínio e cadeias de pensamento de LLMs. |
| **LangWatch** | [langwatch/langwatch](https://github.com/langwatch/langwatch) | Plataforma open-source para observabilidade, testes automatizados e monitoramento de LLMs. |
| **Manacá 1B Base** | [Instituto-IA-LNCC/manaca-1b-base](https://github.com/Instituto-IA-LNCC/manaca-1b-base) | Modelo de linguagem de 1 bilhão de parâmetros treinado pelo LNCC com foco em língua portuguesa. |
| **Ollama** | [ollama/ollama](https://github.com/ollama/ollama) | Padrão da indústria para baixar e rodar modelos locais (Llama 3, DeepSeek, Mistral, Qwen). |
| **OmniRoute** | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | Gateway de IA unificado que conecta 350+ provedores e faz fallback inteligente de cotas e erros. |
| **Open WebUI** | [open-webui/open-webui](https://github.com/open-webui/open-webui) | Interface web auto-hospedada completa estilo ChatGPT, com suporte a Ollama, RAG e agentes. |
| **Open-Notebook** | [lfnovo/open-notebook](https://github.com/lfnovo/open-notebook) | Caderno de estudos inteligente com RAG multi-documento para síntese e perguntas sobre PDFs (alternativa ao NotebookLM). |
| **OpenViking** | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | Engine de alta performance da ByteDance para inferência, decodificação e paralelismo de modelos de IA. |
| **Overmind** | [overmind-core/overmind](https://github.com/overmind-core/overmind) | Stack que transforma dados de agentes em modelos especializados para tarefas específicas via fine-tuning. |
| **RAGFlow** | [infiniflow/ragflow](https://github.com/infiniflow/ragflow) | Motor de RAG open-source de nível corporativo com compreensão profunda de documentos complexos e interface de chat. |
| **TensorZero** | [tensorzero/tensorzero](https://github.com/tensorzero/tensorzero) | Gateway e infraestrutura open-source para otimização, feedback e orquestração de LLMs em produção. |
| **Unsloth** | [unslothai/unsloth](https://github.com/unslothai/unsloth) | Biblioteca de fine-tuning ultrarrápida que reduz uso de VRAM em 80% e acelera treinamento em 2x a 5x. |
| **WhichLLM** | [Andyyyy64/whichllm](https://github.com/Andyyyy64/whichllm) | CLI que detecta a CPU/GPU/RAM da sua máquina e indica exatamente quais modelos rodam com boa velocidade. |
| **Xerj** | [xerj-org/xerj](https://github.com/xerj-org/xerj) | Mecanismo de busca local-first e servidor MCP para agentes de IA em binário único Rust, oferecendo busca híbrida BM25 + vetorial, memória contínua para agentes e RAG ultrarrápido sem dependência de nuvem. |

---

<a id="categoria-3"></a>
### 3. 👁️ Visão Computacional, IA Visual & 3D
*Detecção de objetos, segmentação semântica, modelos de difusão de imagem, sensoriamento espacial e geração de ativos 3D.*

| Projeto | Repositório Oficial | Descrição |
|---|---|---|
| **Detectron2** | [facebookresearch/detectron2](https://github.com/facebookresearch/detectron2) | Plataforma de visão computacional da Meta para detecção de objetos de ponta, segmentação de instâncias e segmentação panóptica. |
| **Diffusers** | [huggingface/diffusers](https://github.com/huggingface/diffusers) | A biblioteca padrão da indústria para modelos de difusão de imagem, áudio e vídeo da Hugging Face. |
| **EchoMimic** | [BadToBest/EchoMimic](https://github.com/BadToBest/EchoMimic) | Geração de animações de retrato realistas sincronizadas com áudio e pontos de referência facial. |
| **Fooocus** | [lllyasviel/Fooocus](https://github.com/lllyasviel/Fooocus) | Interface simplificada e otimizada para geração de imagens de alta qualidade com SDXL (alternativa local ao Midjourney). |
| **LivePortrait** | [KwaiVGI/LivePortrait](https://github.com/KwaiVGI/LivePortrait) | Anima retratos e fotos estáticas reproduzindo expressões faciais e movimentos de vídeo de referência. |
| **RuView** | [ruvnet/RuView](https://github.com/ruvnet/RuView) | Transforma sinais Wi-Fi em inteligência espacial em tempo real, presença e monitoramento sem câmeras. |
| **SadTalker** | [OpenTalker/SadTalker](https://github.com/OpenTalker/SadTalker) | Produz vídeos de cabeças falantes (Talking Heads) a partir de uma foto e um áudio de voz. |
| **spritefusion-sprite-normals** | [Hugo-Dz/spritefusion-sprite-normals](https://github.com/Hugo-Dz/spritefusion-sprite-normals) | Ferramenta em Rust para geração automática de normal maps com iluminação dinâmica para sprites 2D e spritesheets de jogos. |
| **TRELLIS.2** | [microsoft/TRELLIS.2](https://github.com/microsoft/TRELLIS.2) | Modelo de ponta da Microsoft para geração de ativos 3D de alta fidelidade a partir de imagens e texto. |
| **Upscayl** | [upscayl/upscayl](https://github.com/upscayl/upscayl) | Upscaler de imagens e fotos via inteligência artificial gratuito e de código aberto para desktop (macOS, Linux e Windows), com múltiplos modelos de super-resolução. |
| **WiFi DensePose** | [superstar1225/DensePose_from_WiFi](https://github.com/superstar1225/DensePose_from_WiFi) | Rastreia a posição e postura corporal de pessoas através de paredes utilizando interferência de sinal Wi-Fi. |

---

<a id="categoria-4"></a>
### 4. 🌐 Automação de Navegador & Web Scraping
*Robôs, crawlers inteligentes e navegadores desenvolvidos para navegar e extrair dados sem bloqueios.*

| Projeto | Repositório Oficial | Descrição |
|---|---|---|
| **AutoScraper** | [alirezamika/autoscraper](https://github.com/alirezamika/autoscraper) | Scraper inteligente e automático para Python que aprende a extrair dados baseado em poucos exemplos. |
| **Browser-Use** | [browser-use/browser-use](https://github.com/browser-use/browser-use) | Torna qualquer site acessível para agentes de IA interagirem como humanos usando visão e árvore DOM. |
| **Camofox** | [redf0x1/camofox-browser](https://github.com/redf0x1/camofox-browser) | Navegador anti-detecção baseado no motor Camoufox com servidor MCP para agentes evitarem bloqueios. |
| **Camofox Browser** | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | Navegador headless furtivo projetado para agentes de IA burlarem Cloudflare, proteções antibot e bloqueios de scraping sem esforço. |
| **Crawl4AI** | [unclecode/crawl4ai](https://github.com/unclecode/crawl4ai) | Crawler e scraper web ultra-rápido projetado especialmente para alimentar LLMs e pipelines de RAG. |
| **Crawlee** | [apify/crawlee](https://github.com/apify/crawlee) | Biblioteca avançada para crawling e scraping web confiável em Node.js e Python com gestão de proxies e fingerprints. |
| **curl-impersonate** | [lexiforest/curl-impersonate](https://github.com/lexiforest/curl-impersonate) | Build especial do curl que mimetiza assinaturas TLS/HTTP2 de navegadores reais para evitar bloqueios. |
| **Google Maps Scraper** | [omkarcloud/google-maps-scraper](https://github.com/omkarcloud/google-maps-scraper) | Raspador eficiente de dados públicos de empresas, telefones e e-mails listados no Google Maps. |
| **Google Maps Scraper** | [gosom/google-maps-scraper](https://github.com/gosom/google-maps-scraper) | Scraper de alto desempenho para extrair dados completos de empresas no Google Maps (endereço, telefone, website, avaliações, latitude/longitude). |
| **OpenCLI** | [jackwener/opencli](https://github.com/jackwener/opencli) | Transforma qualquer site em CLI e permite que agentes de IA usem a sessão autenticada do seu navegador. |
| **PinchTab** | [pinchtab/pinchtab](https://github.com/pinchtab/pinchtab) | Bridge de automação de navegador ultraleve em Go para agentes de IA, com injeção furtiva anti-detecção e baixo consumo de tokens. |
| **Scrapling** | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | Biblioteca Python para web scraping adaptativo com bypass inteligente de defesas anti-bot. |
| **Scrapy** | [scrapy/scrapy](https://github.com/scrapy/scrapy) | O mais consagrado e maduro framework de web crawling e extração de dados para Python. |
| **Stagehand** | [browserbase/stagehand](https://github.com/browserbase/stagehand) | SDK de automação de navegador com IA que quebra menos e se adapta a mudanças de interface. |

---

<a id="categoria-5"></a>
### 5. 🎬 Geração & Edição de Áudio, Vídeo e Voz
*Criação programática de vídeos, animações, síntese e clonagem de voz ultra-realistas, transcrição e manipulação de mídia.*

| Projeto | Repositório Oficial | Descrição |
|---|---|---|
| **Auto-Editor** | [WyattBlue/auto-editor](https://github.com/WyattBlue/auto-editor) | Ferramenta de linha de comando para edição automatizada de vídeo e áudio, cortando silêncios e pausas sem intervenção manual. |
| **ChatTTS** | [2noise/ChatTTS](https://github.com/2noise/ChatTTS) | Modelo de conversação texto-para-fala de altíssima qualidade com entonações, pausas e risadas naturais. |
| **Cobalt** | [imputnet/cobalt](https://github.com/imputnet/cobalt) | Ferramenta moderna, limpa e sem anúncios para baixar mídias e vídeos de redes sociais e plataformas de streaming. |
| **Gallery-dl** | [mikf/gallery-dl](https://github.com/mikf/gallery-dl) | Utilitário de linha de comando para download automatizado de galerias completas de imagens de dezenas de plataformas e fóruns. |
| **Ghost Downloader 3** | [XiaoYouChR/Ghost-Downloader-3](https://github.com/XiaoYouChR/Ghost-Downloader-3) | Gerenciador e acelerador de download modular de código aberto com suporte a múltiplos protocolos. |
| **HyperFrames** | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | Framework de renderização determinística que transforma código web e animações em vídeo MP4. |
| **Hypit** | [hypit-ai/hypit](https://github.com/hypit-ai/hypit) | Pega vídeos de referência de alta performance e clona sua estrutura em código editável por IA. |
| **Lazy-Frames** | [cosmicstack-labs/lazy-frames](https://github.com/cosmicstack-labs/lazy-frames) | Workflow local alimentado por agentes de IA para criar e renderizar animações em MP4. |
| **MoneyPrinterTurbo** | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | Automação completa para geração de vídeos curtos em alta resolução para TikTok, Shorts e Reels com um único clique a partir de temas ou palavras-chave. |
| **MoneyPrinterV2** | [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | Gerador automatizado de vídeos curtos (Shorts/Reels) com narração, legendas e B-roll por IA. |
| **Open-Generative-AI** | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | Estúdio de código aberto para geração e manipulação de mídia, imagens e vídeos com múltiplos modelos. |
| **Pipecat** | [pipecat-ai/pipecat](https://github.com/pipecat-ai/pipecat) | Framework open-source de produção para agentes de voz e IA multimodal em tempo real. |
| **spotDL** | [spotDL/spotify-downloader](https://github.com/spotDL/spotify-downloader) | Ferramenta CLI de alta performance para baixar músicas, álbuns e playlists inteiras do Spotify em MP3/FLAC com metadados oficiais, letras e capa em alta resolução embutidos. |
| **VoiceStudio** | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | Suíte open-source e 100% local com mais de 78 mil estrelas para clonagem de voz, design vocal, dublagem de vídeos, ditado e geração de audiobooks em mais de 640 idiomas. |
| **VoxCPM** | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | Modelo de síntese de voz (TTS) de última geração sem tokenizador para clonagem de voz ultra-realista e fala multilíngue com alta expressividade. |
| **Whisper** | [openai/whisper](https://github.com/openai/whisper) | Modelo de reconhecimento e transcrição de fala em áudio e múltiplos idiomas de alta precisão. |
| **yt-dlp** | [yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp) | Utilitário de linha de comando padrão da indústria para download e extração de vídeos e áudio da web. |

---

<a id="categoria-6"></a>
### 6. 🎨 Design, Prototipagem & Arquitetura Visual
*Modelagem visual de sistemas, diagramas Entidade-Relacionamento, wireframes, design systems e prototipagem UI/UX.*

| Projeto | Repositório Oficial | Descrição |
|---|---|---|
| **Archify** | [tt-a1i/archify](https://github.com/tt-a1i/archify) | Skill de agente para geração de diagramas de arquitetura, fluxo e ciclo de vida em HTML interativo com animações. |
| **Diagram Design** | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | Design editorial e estruturado de 42 tipos de diagramas em HTML + SVG nativo para Claude Code, Codex, Cursor e agentes de IA sem depender de Mermaid. |
| **DrawDB** | [drawdb-io/drawdb](https://github.com/drawdb-io/drawdb) | Modelador de diagramas Entidade-Relacionamento (ERD) direto no navegador com exportação SQL. |
| **Excalidraw** | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw) | Quadro branco virtual infinito para diagramação e colaboração visual com estilo desenhado à mão. |
| **HTML Anything** | [nexu-io/html-anything](https://github.com/nexu-io/html-anything) | Editor agentic de HTML com 75 skills para criar apresentações, relatórios e páginas direto via agentes de IA. |
| **Penpot** | [penpot/penpot](https://github.com/penpot/penpot) | Plataforma colaborativa de design de interface e prototipagem baseada em padrões web (alternativa ao Figma). |
| **SolidCraft** | [tangency-labs/solidcraft](https://github.com/tangency-labs/solidcraft) | Software CAD 3D paramétrico open-source desenvolvido em Rust puro para desktop e web, com integração direta ao protocolo MCP para geração e edição de modelos 3D via agentes de IA. |

---

<a id="categoria-7"></a>
### 7. 📱 Mobile, Android & Emulação
*Ferramentas de engenharia mobile, espelhamento e controle de dispositivos, emuladores Android e arquitetura iOS/Swift.*

| Projeto | Repositório Oficial | Descrição |
|---|---|---|
| **Andronix** | [AndronixApp/AndronixCore](https://github.com/AndronixApp/AndronixCore) | Permite instalar distribuições Linux completas (Ubuntu, Debian, Manjaro) no Android sem necessidade de root. |
| **AppAgent** | [mnotgod96/AppAgent](https://github.com/mnotgod96/AppAgent) | Agente multimodal que aprende e opera aplicativos Android como um humano. |
| **Artemis (Google)** | [google/artemis](https://github.com/google/artemis) | Framework oficial da Google que transforma comandos em linguagem natural em automação confiável no Android, com 99%+ de taxa de sucesso no benchmark AndroidWorld e integração nativa com assistentes de IA (Antigravity, Claude Code, Codex). |
| **Awesome iOS Architecture** | [onmyway133/awesome-ios-architecture](https://github.com/onmyway133/awesome-ios-architecture) | Coletânea curada com as melhores arquiteturas, padrões (MVVM-C, VIPER, Clean) e boas práticas para iOS. |
| **Design Patterns in Swift** | [ochococo/Design-Patterns-In-Swift](https://github.com/ochococo/Design-Patterns-In-Swift) | Implementação prática e idiomática dos 23 padrões de projeto (GoF) em Swift 5.0. |
| **dex2jar** | [pxb1988/dex2jar](https://github.com/pxb1988/dex2jar) | Ferramentas essenciais para trabalhar com arquivos Android .dex e converter para classes Java (.class / .jar). |
| **docker-android** | [HQarroum/docker-android](https://github.com/HQarroum/docker-android) | Imagem Docker personalizável que roda emuladores Android completos como um microserviço. |
| **iOS Lead Interview Guide** | [shobhakartiwari/iOS_Lead_Interview](https://github.com/shobhakartiwari/iOS_Lead_Interview) | Guia técnico avançado de arquitetura, concorrência, memória e perguntas para entrevistas de liderança iOS. |
| **IOSSecuritySuite** | [securing/IOSSecuritySuite](https://github.com/securing/IOSSecuritySuite) | Biblioteca open-source em Swift para segurança mobile: detecção de jailbreak, anti-debug, hooks e integridade. |
| **LibrePods** | [librepods-org/librepods](https://github.com/librepods-org/librepods) | Liberta os AirPods do ecossistema Apple, trazendo controle de áudio espacial, cancelamento de ruído e status de bateria para Linux e Android. |
| **OWASP MSTG** | [OWASP/owasp-mstg](https://github.com/OWASP/owasp-mstg) | Guia oficial da OWASP de testes de segurança, engenharia reversa e pentest em aplicativos móveis. |
| **scrcpy** | [Genymobile/scrcpy](https://github.com/Genymobile/scrcpy) | Espelhamento e controle de alta performance de dispositivos Android via USB/Wi-Fi com baixa latência. |
| **Termux** | [termux/termux-app](https://github.com/termux/termux-app) | Emulador de terminal que traz um ecossistema Linux completo para dispositivos Android sem root. |

---

<a id="categoria-8"></a>
### 8. 🛡️ Cibersegurança, Pentest & OSINT
*Investigação de fontes abertas, análise de redes, engenharia reversa e testes de intrusão éticos.*

| Projeto | Repositório Oficial | Descrição |
|---|---|---|
| **Anthropic Cybersecurity Skills** | [liptonj-eng/anthropic-cybersecurity-skills](https://github.com/liptonj-eng/anthropic-cybersecurity-skills) | Mais de 730 skills estruturadas de cibersegurança e pentest mapeadas pelo MITRE ATT&CK para agentes autônomos. |
| **Atomic Red Team** | [redcanaryco/atomic-red-team](https://github.com/redcanaryco/atomic-red-team) | Biblioteca de testes automatizados e simulações de adversários de alta precisão mapeada diretamente na matriz MITRE ATT&CK para validação de segurança. |
| **Awesome Hacking** | [Hack-with-Github/Awesome-Hacking](https://github.com/Hack-with-Github/Awesome-Hacking) | Coleção curada com os melhores repositórios, ferramentas e tutoriais de segurança ofensiva e defensiva. |
| **Awesome OSINT** | [jivoi/awesome-osint](https://github.com/jivoi/awesome-osint) | Diretório completo de ferramentas de coleta e inteligência de fontes públicas (Open Source Intelligence). |
| **Codex Security** | [openai/codex-security](https://github.com/openai/codex-security) | Framework e recomendações de segurança da OpenAI para execução de coding agents em ambientes de produção. |
| **CyberChef** | [gchq/CyberChef](https://github.com/gchq/CyberChef) | Suíte web multiuso do GCHQ britânico para criptografia, encoding, compressão, desofuscação e análise profunda de dados e payloads cibernéticos. |
| **Domain Digger** | [wotschofsky/domain-digger](https://github.com/wotschofsky/domain-digger) | Toolkit de inteligência de fontes abertas (OSINT) e análise abrangente de domínios, DNS, subdomínios, registros e pegada digital. |
| **ESP32-BlueJammer** | [EmenstaNougat/ESP32-BlueJammer](https://github.com/EmenstaNougat/ESP32-BlueJammer) | Utilitário para testes de intrusão e estresse de rádio frequência 2.4GHz (Bluetooth/BLE/WiFi) utilizando ESP32 e módulos nRF24. |
| **Fieldwatch** | [OffGridPete/Fieldwatch](https://github.com/OffGridPete/Fieldwatch) | Observador passivo e seguro de transmissões Wi-Fi e Bluetooth LE para Android. |
| **Flowsint** | [reconurge/flowsint](https://github.com/reconurge/flowsint) | Plataforma visual baseada em grafos para investigações de inteligência cibernética, análise de vínculos e correlação de entidades em OSINT. |
| **Kali NetHunter** | [offensive-security/kali-nethunter](https://github.com/offensive-security/kali-nethunter) | Sistema operacional Kali Linux adaptado para smartphones Android (ver também [GitLab oficial](https://gitlab.com/kalilinux/nethunter/)). |
| **Metasploit** | [rapid7/metasploit-framework](https://github.com/rapid7/metasploit-framework) | O framework de testes de invasão e validação de vulnerabilidades mais utilizado no mundo. |
| **MVT (Mobile Verification Toolkit)** | [mvt-project/mvt](https://github.com/mvt-project/mvt) | Kit forense open-source para análise e detecção de spywares sofisticados (como Pegasus) em smartphones. |
| **Netryx Astra V2** | [sparkyniner/Netryx-Astra-V2-Geolocation-Tool](https://github.com/sparkyniner/Netryx-Astra-V2-Geolocation-Tool) | Ferramenta avançada de geolocalização e inteligência de imagens ao nível da rua para investigação OSINT. |
| **Nmap** | [nmap/nmap](https://github.com/nmap/nmap) | O utilitário padrão para exploração de rede, descoberta de portas abertas e auditoria de serviços. |
| **OSINT Framework** | [lockfale/osint-framework](https://github.com/lockfale/osint-framework) | Mapa interativo e estruturado de fontes de dados e ferramentas de pesquisa de inteligência online. |
| **OWASP ZAP** | [zaproxy/zaproxy](https://github.com/zaproxy/zaproxy) | Scanner gratuito e de código aberto para encontrar falhas de segurança em aplicações web. |
| **PhoneInfoga** | [sundowndev/phoneinfoga](https://github.com/sundowndev/phoneinfoga) | Ferramenta avançada para escaneamento e rastreamento de informações sobre números de telefone. |
| **Pwdb-Public** | [FlameOfIgnis/Pwdb-Public](https://github.com/FlameOfIgnis/Pwdb-Public) | Dataset e utilitários para análise forense e auditoria de credenciais vazadas em pentest defensivo. |
| **Rea** | [morluto/rea](https://github.com/morluto/rea) | Engenharia reversa automatizada com agentes de IA, capaz de dissecar desde comportamento de aplicações até descompilação de binários nativos. |
| **Security Audit Skill** | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | Agent skill oficial da Cloudflare para coding agents realizarem auditorias automatizadas de segurança de ponta a ponta com achados estruturados e verificáveis. |
| **Sherlock** | [sherlock-project/sherlock](https://github.com/sherlock-project/sherlock) | Localiza perfis e contas de um mesmo nome de usuário em centenas de redes sociais simultaneamente. |
| **Sigma** | [SigmaHQ/sigma](https://github.com/SigmaHQ/sigma) | Padrão genérico e aberto de assinaturas de detecção de ameaças aplicável a múltiplos mecanismos SIEM (Splunk, Elastic, QRadar, Wazuh). |
| **Strix** | [usestrix/strix](https://github.com/usestrix/strix) | Scanner de vulnerabilidades e segurança ofensiva automatizado para aplicações web e APIs. |
| **Wazuh** | [wazuh/wazuh](https://github.com/wazuh/wazuh) | Plataforma unificada de código aberto para SIEM e XDR que oferece detecção de ameaças, monitoramento de integridade e resposta a incidentes em tempo real. |
| **Wifit3** | [derv82/wifit3](https://github.com/derv82/wifit3) | Ferramenta moderna e multiplataforma (Linux, macOS, Windows) para auditoria e testes automatizados de segurança e pentest em redes Wi-Fi via adaptadores USB. |
| **Wireshark** | [wireshark/wireshark](https://github.com/wireshark/wireshark) | O analisador de protocolos de rede e captura de pacotes em tempo real mais respeitado do setor. |

---

<a id="categoria-9"></a>
### 9. 💻 Ferramentas de Desenvolvimento & Terminal
*Utilitários que aumentam a produtividade diária de desenvolvedores, clientes de banco de dados e melhorias de fluxo.*

| Projeto | Repositório Oficial | Descrição |
|---|---|---|
| **Awesome Rust** | [rust-unofficial/awesome-rust](https://github.com/rust-unofficial/awesome-rust) | Curadoria definitiva com as melhores bibliotecas, ferramentas de sistema e recursos do ecossistema Rust. |
| **ccusage** | [ccusage/ccusage](https://github.com/ccusage/ccusage) | Ferramenta CLI interativa para monitorar em tempo real o consumo de tokens, custos acumulados e limites de uso do Claude Code e assistentes de IA. |
| **Code-Server** | [coder/code-server](https://github.com/coder/code-server) | Execute o VS Code completo diretamente no navegador em qualquer servidor remoto e acesse seu ambiente de desenvolvimento de qualquer lugar. |
| **Daytona** | [daytonaio/daytona](https://github.com/daytonaio/daytona) | Gerenciador de ambientes de desenvolvimento padronizados e workspaces seguros (alternativa ao GitHub Codespaces). |
| **DBX** | [t8y2/dbx](https://github.com/t8y2/dbx) | Cliente de banco de dados ultrarrápido em Rust (15-20 MB), compatível com 70+ bancos, IA e MCP. |
| **DevTUI** | [skatkov/devtui](https://github.com/skatkov/devtui) | Canivete suíço no terminal com utilitários de conversão, decodificação, JWT, hash e inspeção rápida para devs. |
| **ElysiaJS** | [elysiajs/elysia](https://github.com/elysiajs/elysia) | Framework web TypeScript ergonômico e com desempenho recorde projetado para o runtime Bun. |
| **GH-Dash** | [dlvhdr/gh-dash](https://github.com/dlvhdr/gh-dash) | Painel interativo dentro do terminal para gerenciar Pull Requests e Issues do GitHub sem usar o browser. |
| **GitIngest** | [coderamp-labs/gitingest](https://github.com/coderamp-labs/gitingest) | Substitui "hub" por "ingest" em qualquer URL do GitHub para gerar um extrato de código formatado e otimizado para contexto em prompts de LLMs. |
| **Markdoc** | [markdoc/markdoc](https://github.com/markdoc/markdoc) | Poderoso framework de autoria baseado em Markdown criado pela Stripe para criação de documentações técnicas customizadas e extensíveis. |
| **mirrord** | [metalbear-co/mirrord](https://github.com/metalbear-co/mirrord) | Conecta processos locais ao seu cluster cloud para rodar e debugar código local sob condições reais de nuvem. |
| **Open Code Review** | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | CLI de code review inteligente da Alibaba que combina regras determinísticas rápidas com LLMs. |
| **Pake** | [tw93/Pake](https://github.com/tw93/Pake) | Utilitário em Rust/Tauri que transforma qualquer página web ou ferramenta em um aplicativo desktop nativo e ultraleve (<10 MB), substituindo wrappers Electron pesados. |
| **Public APIs** | [public-apis/public-apis](https://github.com/public-apis/public-apis) | Catálogo com milhares de APIs públicas gratuitas para desenvolvedores integrarem em projetos. |
| **Repsy** | [repsyio/repsy](https://github.com/repsyio/repsy) | Repositório e gerenciador centralizado de artefatos de build (Maven, npm, PyPI, etc.). |
| **RTK (Rust Token Killer)** | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | Proxy CLI em Rust que intercepta e comprime em 60-90% as saídas de comandos do terminal (git, grep, testes, logs) antes de entrarem no contexto de agentes de IA. |
| **System Design Primer** | [donnemartin/system-design-primer](https://github.com/donnemartin/system-design-primer) | O guia de referência definitivo para estudo de arquitetura, escalabilidade e design de sistemas complexos. |
| **Tinycast** | [abue-ammar/tinycast](https://github.com/abue-ammar/tinycast) | Lançador nativo ultraleve para macOS (<100 MB de RAM) capaz de executar extensões da Raycast. |
| **Vizro** | [mckinsey/vizro](https://github.com/mckinsey/vizro) | Framework modular da McKinsey para criação rápida de dashboards de dados interativos com Python. |
| **windows95** | [felixrieseberg/windows95](https://github.com/felixrieseberg/windows95) | Emulação completa do sistema operacional Windows 95 em Electron empacotada como app para macOS, Linux e Windows. |
| **witr** | [pranshuparmar/witr](https://github.com/pranshuparmar/witr) | CLI e TUI interativa ("Why is this running?") para rastrear qualquer processo, porta aberta, container ou arquivo até o comando raiz que o originou. |

---

<a id="categoria-10"></a>
### 10. ⚙️ Workflows, Orquestração & DevOps
*Ferramentas para automação de tarefas em lote, gerenciamento de infraestrutura, DAGs e pipelines.*

| Projeto | Repositório Oficial | Descrição |
|---|---|---|
| **Activepieces** | [activepieces/activepieces](https://github.com/activepieces/activepieces) | Plataforma open-source de automação de fluxos de IA com suporte nativo a centenas de servidores MCP. |
| **Awesome Harness Engineering** | [yenanjing/awesome-harness-engineering](https://github.com/yenanjing/awesome-harness-engineering) | Guia com mais de 80 repositórios sobre engenharia de testes, harnesses de avaliação de agentes e frameworks de CI/CD. |
| **Coolify** | [coollabsio/coolify](https://github.com/coollabsio/coolify) | Plataforma self-hosted tudo-em-um para gerenciar deploys de apps, bancos de dados e serviços (alternativa ao Heroku/Vercel). |
| **Dagu** | [dagu-org/dagu](https://github.com/dagu-org/dagu) | Orquestrador leve e database-free para rodar DAGs declarativas em YAML; alternativa direta ao Airflow e Cron. |
| **Fleetbase** | [fleetbase/fleetbase](https://github.com/fleetbase/fleetbase) | Sistema operacional modular open-source para gestão de frotas, entregas e supply chain. |
| **FreeDomain** | [DigitalPlatDev/FreeDomain](https://github.com/DigitalPlatDev/FreeDomain) | Plataforma e recursos práticos para registro gratuito de domínios com suporte a nameservers customizados e guias de DNS. |
| **Homelab GitOps IaC** | [Mafyuh/iac](https://github.com/Mafyuh/iac) | Exemplo completo de Infrastructure as Code (IaC) orientada a GitOps para infraestrutura e servidores locais. |
| **Nango** | [NangoHQ/nango](https://github.com/NangoHQ/nango) | Plataforma de infraestrutura de integrações e autenticação OAuth unificada para conectar agentes de IA e aplicações a mais de 1.000 APIs externas. |
| **NetBox** | [netbox-community/netbox](https://github.com/netbox-community/netbox) | A principal ferramenta de documentação e fonte de verdade (DCIM/IPAM) para redes de computadores. |
| **Uniterm** | [uniterm-app/uniterm](https://github.com/uniterm-app/uniterm) | Aplicativo que suporta mais de 30 protocolos de conexão e permite que agentes de IA rodem comandos shell. |

---

<a id="categoria-11"></a>
### 11. 🏠 Substitutos Open-Source de Apps Pagos (Self-Hosted)
*Alternativas gratuitas e auto-hospedadas para economizar nas assinaturas de serviços e SaaS populares.*

| Projeto | Repositório Oficial | O que substitui | Descrição |
|---|---|---|---|
| **9Drive** | [zenhosta/9drive](https://github.com/zenhosta/9drive) | Google One, Dropbox Plus | Gateway de armazenamento web self-hosted que conecta múltiplas contas do Google Drive em um único painel virtual, unificando cotas e roteando uploads para onde houver espaço livre. |
| **Anytype** | [anyproto/anytype-ts](https://github.com/anyproto/anytype-ts) | SaaS pago | Espaço de trabalho local e criptografado para notas, tarefas e grafos de conhecimento com arquitetura P2P. |
| **Apache Cloudberry** | [apache/cloudberry](https://github.com/apache/cloudberry) | Greenplum, Snowflake | Banco de dados analítico de processamento massivo paralelo (MPP) maduro e open-source para Big Data e Data Warehouses. |
| **AppFlowy** | [AppFlowy-IO/AppFlowy](https://github.com/AppFlowy-IO/AppFlowy) | Notion | Espaço de trabalho seguro e local para notas, quadros Kanban e documentação. |
| **ArchiveBox** | [ArchiveBox/ArchiveBox](https://github.com/ArchiveBox/ArchiveBox) | Wayback Machine, Pocket, Pinboard | Solução completa e auto-hospedada de arquivamento web (salva páginas, PDFs, HTML, mídias e capturas com replay offline). |
| **Audiobookshelf** | [advplyr/audiobookshelf](https://github.com/advplyr/audiobookshelf) | Audible | Servidor auto-hospedado para organizar e ouvir audiolivros e podcasts (alternativa ao Audible). |
| **Cal.com** | [calcom/cal.com](https://github.com/calcom/cal.com) | Calendly | Plataforma completa de agendamento de eventos e reuniões com integrações de calendário (alternativa ao Calendly). |
| **Cap** | [CapSoftware/Cap](https://github.com/CapSoftware/Cap) | Loom | Gravador de tela open-source leve e compartilhável instantaneamente. |
| **ChangeDetection.io** | [dgtlmoon/changedetection.io](https://github.com/dgtlmoon/changedetection.io) | Visualping, Distill.io | Ferramenta self-hosted para monitoramento contínuo de alterações em páginas web, quedas de preço e alertas de estoque em tempo real. |
| **Docmost** | [docmost/docmost](https://github.com/docmost/docmost) | Notion e confluence | Wiki e plataforma de documentação colaborativa em tempo real para times (alternativa ao Notion e Confluence). |
| **EdgeEver** | [edgeever/edgeever](https://github.com/edgeever/edgeever) | Evernote | Aplicativo de anotações em três colunas que roda na infraestrutura gratuita da Cloudflare. |
| **Home Assistant** | [home-assistant/core](https://github.com/home-assistant/core) | SaaS pago | O principal ecossistema de automação residencial de código aberto focado em controle local e privacidade. |
| **Immich** | [immich-app/immich](https://github.com/immich-app/immich) | Google Fotos | Backup de fotos com reconhecimento facial, mapas e pesquisa sem custos de nuvem. |
| **Jellyfin** | [jellyfin/jellyfin](https://github.com/jellyfin/jellyfin) | Plex, Emby | Servidor de streaming de mídia self-hosted 100% gratuito e open-source para organizar e transmitir filmes, séries e músicas para qualquer dispositivo. |
| **Joplin** | [laurent22/joplin](https://github.com/laurent22/joplin) | Evernote, Notion, OneNote | Aplicativo de notas e gerenciamento de tarefas focado em privacidade, com suporte a Markdown, multimídia, sincronização em nuvem própria e criptografia E2EE. |
| **KaraKeep** | [karakeep-app/karakeep](https://github.com/karakeep-app/karakeep) | Raindrop, Pocket, Notion Clipper | Aplicativo self-hosted para salvar tudo (links, notas, imagens) com auto-tagging por IA e busca textual profunda. |
| **LibreChat** | [LibreChat-AI/LibreChat](https://github.com/LibreChat-AI/LibreChat) | ChatGPT Plus, Claude Pro, Poe | Interface web open-source definitiva para múltiplos modelos de IA com suporte nativo a MCP (Model Context Protocol), Code Interpreter, Artifacts e autenticação multiusuário. |
| **LibreTranslate** | [LibreTranslate/LibreTranslate](https://github.com/LibreTranslate/LibreTranslate) | Google Translate API, DeepL | API e motor de tradução automática 100% open-source, auto-hospedável e offline, sem chaves pagas nem envio de dados para nuvem. |
| **LocalSend** | [localsend/localsend](https://github.com/localsend/localsend) | AirDrop, WeTransfer | Alternativa open-source, segura e multiplataforma ao AirDrop para compartilhamento direto de arquivos via rede local sem nuvem. |
| **Maybe Finance** | [maybe-finance/maybe](https://github.com/maybe-finance/maybe) | Copilot / Monarch Money | Aplicativo open-source e auto-hospedado de gestão financeira pessoal e controle de patrimônio. |
| **Memos** | [usememos/memos](https://github.com/usememos/memos) | SaaS pago | Ambiente leve para anotações rápidas e microblogging com total privacidade e auto-hospedagem. |
| **n8n** | [n8n-io/n8n](https://github.com/n8n-io/n8n) | Zapier / Make | Plataforma de automação visual de fluxos de trabalho com centenas de integrações. |
| **NocoDB** | [nocodb/nocodb](https://github.com/nocodb/nocodb) | Airtable | Transforma qualquer banco de dados relacional (MySQL, Postgres, etc.) em interface de planilha inteligente (alternativa ao Airtable). |
| **NZBdav** | [nzbdav/nzbdav](https://github.com/nzbdav/nzbdav) | Armazenamento local | Monta arquivos do Usenet como unidade virtual para streaming no Sonarr/Radarr. |
| **Oomwoo** | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | iRobot Roomba, Roborock | Aspirador robô totalmente open-source com navegação LiDAR SLAM, ROS2, ESP32, Raspberry Pi e integração nativa com o Home Assistant para automação residencial livre de nuvem proprietária. |
| **Open SaaS** | [wasp-lang/open-saas](https://github.com/wasp-lang/open-saas) | SaaS Boilerplates pagos ($200+) | Boilerplate full-stack 100% gratuito (React, NodeJS, Prisma, Stripe) com autenticação, pagamentos, tarefas em background e suporte nativo a agentes de IA. |
| **OpenPanel** | [openpanel-dev/openpanel](https://github.com/openpanel-dev/openpanel) | Mixpanel, Amplitude | Plataforma self-hosted de analytics de produto e tráfego web moderna e focada em privacidade, alternativa direta ao Mixpanel e Amplitude. |
| **OpenWA** | [rmyndharis/OpenWA](https://github.com/rmyndharis/OpenWA) | Twilio / Z-API | Gateway de API do WhatsApp gratuito, auto-hospedado e de código aberto para envio e recebimento de mensagens. |
| **Paperless-ngx** | [paperless-ngx/paperless-ngx](https://github.com/paperless-ngx/paperless-ngx) | SaaS pago | Indexador e gerenciador de documentos físicos digitalizados com OCR automático e busca instantânea. |
| **Pear Desktop** | [pear-devs/pear-desktop](https://github.com/pear-devs/pear-desktop) | YouTube Music Desktop, Spotify | Player desktop moderno para YouTube Music com bloqueador nativo de anúncios, suporte a temas, letras sincronizadas e plugins. |
| **Plausible Analytics** | [plausible/analytics](https://github.com/plausible/analytics) | SaaS pago | Analytics de sites moderno, ultraleve (<1 KB), sem cookies e em total conformidade com a LGPD/GDPR. |
| **Reactive Resume** | [reactive-resume/reactive-resume](https://github.com/reactive-resume/reactive-resume) | Novoresume, Canva Resumes | Construtor completo de currículos profissionais, gratuito, focado em privacidade, altamente customizável e exportável em PDF. |
| **RustDesk** | [rustdesk/rustdesk](https://github.com/rustdesk/rustdesk) | TeamViewer, AnyDesk | Software de acesso remoto e controle desktop auto-hospedado de alto desempenho desenvolvido em Rust, com criptografia ponta a ponta. |
| **Spotube** | [team-spotube/spotube](https://github.com/team-spotube/spotube) | Spotify Premium | Cliente open-source de música e podcasts para desktop e mobile alternativo ao Spotify, sem anúncios, sem telemetria e com download direto de playlists para ouvir offline. |
| **Stirling-PDF** | [Stirling-Tools/Stirling-PDF](https://github.com/Stirling-Tools/Stirling-PDF) | Adobe Acrobat / iLovePDF | Suíte web local completa para juntar, dividir, comprimir, converter e assinar PDFs. |
| **Supabase** | [supabase/supabase](https://github.com/supabase/supabase) | Firebase | Plataforma de backend completa com PostgreSQL, autenticação, realtime e storage (alternativa ao Firebase). |
| **Suwayomi-Server** | [Suwayomi/Suwayomi-Server](https://github.com/Suwayomi/Suwayomi-Server) | Apps pagos de leitura | Servidor e cliente desktop multiplataforma para leitura de mangás e quadrinhos baseado na arquitetura Tachiyomi. |
| **TREK** | [liketrek/TREK](https://github.com/liketrek/TREK) | TripIt / Notion | Planejador de viagens e roteiros auto-hospedado com mapas interativos, colaboração em tempo real e orçamentos. |
| **Twenty** | [twentyhq/twenty](https://github.com/twentyhq/twenty) | Salesforce / HubSpot | CRM moderno de código aberto projetado para a era da IA, altamente customizável e auto-hospedado. |
| **Umami** | [umami-software/umami](https://github.com/umami-software/umami) | Google Analytics | Analytics de sites simples, rápido, em conformidade com a LGPD e sem coletar dados invasivos. |
| **Vaultwarden** | [dani-garcia/vaultwarden](https://github.com/dani-garcia/vaultwarden) | 1Password / LastPass | Servidor alternativo em Rust compatível com todos os clientes oficiais do Bitwarden. |
| **VERT** | [VERT-sh/VERT](https://github.com/VERT-sh/VERT) | CloudConvert, iLovePDF | Conversor universal de arquivos local-first em WebAssembly; converte documentos, imagens e áudio direto no navegador sem depender de nuvem. |
| **WordCraft** | [storytold/wordcraft](https://github.com/storytold/wordcraft) | Microsoft Word, Google Docs | Reimplementação open-source e de alta fidelidade do Microsoft Word em Rust puro, oferecendo processamento de texto ultrarrápido, offline e compatibilidade nativa com documentos .docx. |

---

<a id="categoria-12"></a>
### 12. 📈 IA para Negócios, Marketing & Finanças
*Aplicações direcionadas para geração de receita, trading algorítmico, SEO, auditoria e análise de mercado.*

| Projeto | Repositório Oficial | Descrição |
|---|---|---|
| **AI Job Search** | [ai-job-search-dev/ai-job-search](https://github.com/ai-job-search-dev/ai-job-search) | Framework autônomo baseado no Claude Code para busca de empregos e automação de candidaturas: avalia vagas, personaliza currículos, redige cartas e prepara entrevistas. |
| **AutoHedge** | [The-Swarm-Corporation/AutoHedge](https://github.com/The-Swarm-Corporation/AutoHedge) | Framework de inteligência de enxame multi-agente para análise automatizada de mercado financeiro e trading. |
| **Awesome Quant** | [wilsonfreitas/awesome-quant](https://github.com/wilsonfreitas/awesome-quant) | Curadoria abrangente de bibliotecas, pacotes e recursos em Python, R e C++ para Finanças Quantitativas e trading algorítmico. |
| **check-if-email-exists** | [reacherhq/check-if-email-exists](https://github.com/reacherhq/check-if-email-exists) | Validador e verificador de existência de e-mails em Rust com backend HTTP, testando MX, SMTP e sintaxe sem enviar mensagens reais. |
| **Claude Ads** | [AgriciDaniel/claude-ads](https://github.com/AgriciDaniel/claude-ads) | Skill para o Claude auditar contas de anúncios (Google, Meta, etc.), detectar desperdícios e sugerir melhorias. |
| **Fincept Terminal** | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | Terminal financeiro desktop com dados de mercado, relatórios de pesquisa e alternativas ao Bloomberg. |
| **FinRL** | [AI4Finance-Foundation/FinRL](https://github.com/AI4Finance-Foundation/FinRL) | Framework para treinamento de agentes de trading algorítmico usando aprendizado por reforço. |
| **GeoLibre** | [opengeos/GeoLibre](https://github.com/opengeos/GeoLibre) | Plataforma GIS cloud-native leve para visualização, exploração e análise de dados geoespaciais. |
| **Google Timeline Visualizer** | [manolotis/google-timeline-visualizer](https://github.com/manolotis/google-timeline-visualizer) | Dashboard interativo para mapear viagens e trajetos exportados do histórico do Google Maps. |
| **Open-SEO** | [every-app/open-seo](https://github.com/every-app/open-seo) | Suíte open-source para auditoria técnica de SEO, análise de palavras-chave e ranqueamento (alternativa ao Semrush). |
| **OpenTerminal** | [ErTasselli/OpenTerminal](https://github.com/ErTasselli/OpenTerminal) | Dashboard interativo de inteligência e trading financeiro no estilo terminal clássico, operando integralmente com dados públicos de mercado sem chaves pagas ou assinaturas. |
| **TradingAgents** | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | Framework multi-agente para trading quantitativo onde equipes autônomas de LLMs colaboram para analisar fundamentos, gráficos técnicos e risco. |
| **Vibe-Trading** | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | Agente autônomo pessoal de trading algorítmico baseado em LLMs com análise multimodal de sentimento de mercado e execução. |

---

<a id="categoria-13"></a>
### 13. 🔒 Privacidade Digital & Anti-Rastreamento
*Extensões, bloqueadores DNS, limpeza de metadados e configurações para fechar as torneiras de coleta de dados de Big Techs.*

| Projeto | Repositório Oficial | Descrição |
|---|---|---|
| **AdGuard Home** | [AdguardTeam/AdGuardHome](https://github.com/AdguardTeam/AdGuardHome) | Servidor DNS local que bloqueia anúncios, rastreadores e phishing para toda a sua rede doméstica. |
| **Arkenfox user.js** | [arkenfox/user.js](https://github.com/arkenfox/user.js) | Arquivo de preferências para tornar o Firefox uma fortaleza contra fingerprinting e rastreamento. |
| **Brave Browser** | [brave/brave-browser](https://github.com/brave/brave-browser) | Navegador com bloqueador nativo de anúncios, anti-fingerprinting e proteção contra rastreadores. |
| **ExifCleaner** | [szTheory/exifcleaner](https://github.com/szTheory/exifcleaner) | Aplicativo desktop open-source para limpeza de metadados EXIF e dados sensíveis de imagens, vídeos e arquivos PDF via arrastar e soltar. |
| **Free-My-TV** | [simbasjungles/free-my-tv](https://github.com/simbasjungles/free-my-tv) | Launcher alternativo open-source, ultrarrápido e livre de anúncios e telemetria para Smart TVs com Google TV, LG webOS e Samsung Tizen, com reversão em um clique. |
| **Privacy Badger** | [EFForg/privacybadger](https://github.com/EFForg/privacybadger) | Extensão da Electronic Frontier Foundation que aprende a bloquear rastreadores invisíveis. |
| **SearXNG** | [searxng/searxng](https://github.com/searxng/searxng) | Metabuscador de internet livre e auto-hospedável que agrega resultados de dezenas de serviços sem rastrear nem traçar perfis. |
| **Syncthing** | [syncthing/syncthing](https://github.com/syncthing/syncthing) | Sincronização contínua e criptografada de arquivos entre dispositivos de ponta a ponta sem servidores centrais. |
| **uBlock Origin** | [gorhill/uBlock](https://github.com/gorhill/uBlock) | Bloqueador de elementos e propagandas altamente eficiente em uso de memória e CPU. |

---

## 🤝 Contribuições

Contribuições são muito bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um Pull Request com novas ferramentas open-source relevantes.
