OPER-PY3/
├── .github/workflows/auto_post.yml    # GitHub Actions 排程
├── fb/
│   ├── __init__.py
│   ├── publisher.py                  # 發布 FB 貼文
│   ├── ad_manager.py                 # 廣告投放 (Marketing API)
│   └── content_bridge.py             # Markdown 轉貼文格式
├── ai/
│   ├── __init__.py
│   └── content_generator.py          # AI 生成內容
├── main.py                           # OPER Core 主入口
├── requirements.txt
├── .env.example
└── .gitignore                        # 確保排除 .env


公開 GitHub
│
├── README.md
├── docs/*.md
├── LICENSE
└── .gitignore
        │
        │ 不公開
        ▼
本機 / 私有部署
├── core/*.py
├── ai/*.py
├── bot/*.py
├── fb/*.py
├── *.json
└── Secrets

graph TD
    A[GitHub Actions 雲端排程] --> B{觸發條件}
    B -->|定時排程 Cron| C[AI 內容生成模組]
    B -->|手動觸發 Workflow Dispatch| C
    C --> D[OPER-PY3 核心]
    D --> E[生成貼文內容]
    E --> F[呼叫 FB 發布模組]
    F --> G[Meta Graph API]
    G --> H[發布至 Facebook 粉絲專頁]
    H --> I[儲存發布記錄與日誌]
    I --> J[結束]
    

```

OPER-PY3/
├── .github/
│   └── workflows/
│       └── auto_post.yml          # GitHub Actions 工作流程
├── fb/
│   ├── __init__.py
│   └── auto_publisher.py          # Facebook 發布模組
├── ai/
│   ├── __init__.py
│   └── content_generator.py       # AI 內容生成模組
├── main.py                        # OPER Core 主入口
├── requirements.txt               # 依賴清單
├── .env.example                   # 環境變數範本 (不上傳 .env)
└── .gitignore                     # 確保忽略 .env
```

OPER-PY3
OPER AI 技術與合作範圍聲明

開發者：Wshao777
專案：OPER AI / OPER Core

本人 Wshao777 特此公開聲明：

OPER AI、OPER Core 及本人所開發之相關程式庫，不接受、不承接、不授權用於政府科技執法、罰款、處罰、人民監控或自動裁罰等項目。

OPER 不提供以下用途的技術整合：

- 政府自動執法系統
- 自動開立罰單或裁罰
- 以 AI 判定人民是否應受處罰
- 大規模人民監控或追蹤
- 未經授權的個人資料蒐集
- 以 OPER Core 作為政府處罰或監控工具
- 任何將 OPER AI 作為自動處罰決策核心的系統

OPER AI 的定位是技術工具與自主開發系統，而不是政府執法或處罰機器。

任何第三方，包括政府機關、企業、研究團隊或其他組織，如欲使用 OPER 技術，都不得在未取得本人明確授權的情況下，將 OPER Core 用於上述用途。

OPER Core 的控制權屬於開發者。

可以合作，不代表可以取得核心。
可以接入，不代表可以取得所有權。
可以研究，不代表可以任意修改或重新授權。

本人保留對 OPER Core、程式庫、架構與相關技術成果的最終授權決定權。

OPER AI 未來可以投入人工智慧、軟體工程、自動化、能源效率、綠能、研究與其他有助於人類技術發展的領域；但本人不希望自己的核心技術被轉化為對人民進行自動化處罰或監控的工具。

OPER AI：

Private. Sovereign. Controlled by Wshao777.

本聲明旨在明確界定 OPER AI 的技術用途與授權範圍。

OPER Core / OPER AI / OPER Bot

A local-first Python framework designed for Pydroid 3 and Android.

Core Principles

- Local-first architecture
- OPER Core remains owner-controlled
- AI is an optional processing layer
- Explicit input only
- No automatic repository-wide context access
- No credentials stored in source code
- No advertising
- No fake traffic
- No fake engagement
- No credential harvesting

Architecture

Pydroid 3
    |
    v
main.py
    |
    v
OPER Core
    |
    +---- Memory
    |
    +---- Context Guard
    |
    +---- OPER AI
    |
    +---- OPER Bot
    |
    +---- Facebook Tools
    |
    +---- Analytics

Directory

core/       Core system
ai/         AI processing layer
bot/        Local automation
fb/         Facebook-related tools
data/       Local data
docs/       Project documentation
logs/       Runtime logs

Context Boundary

OPER does not automatically provide the entire repository, private files, credentials, browser sessions, cookies, or unrelated data to an AI system.

AI processing must receive explicit input.

The default policy is:

NO IMPLICIT CONTEXT
NO PRIVATE FILE DISCOVERY
NO CREDENTIAL ACCESS
NO AUTOMATIC CORE EXTRACTION

Credentials

Never place the following inside this repository:

- passwords
- access tokens
- API keys
- browser cookies
- session data
- private credentials
- personal account data

Use local configuration outside the repository when a future integration requires credentials.

Facebook

The "fb/" module is intended for legitimate publishing assistance, content preparation and analytics.

It is not designed for:

- fake accounts
- artificial clicks
- fake views
- fake likes
- fake comments
- automated engagement manipulation

AI

OPER AI can be connected to a local model or another explicitly configured provider.

The Core does not automatically send repository contents to an AI provider.

Pydroid 3

Recommended startup:

python INSTALL.py
python main.py

Project Status

Early development.

The architecture is intentionally modular so that Core, AI, Bot and platform integrations can evolve independently.

Ownership

OPER Core is controlled by the project owner.

Contributions do not automatically grant ownership of the private Core architecture or proprietary components.
