ALLOWED_EXTENSIONS = {
    ".py",
    ".md",
    ".txt",
    ".json",
    ".yaml",
    ".yml",
    ".toml",
    ".gitignore",
}

BLOCKED_EXTENSIONS = {
    ".exe",
    ".dll",
    ".bat",
    ".cmd",
    ".ps1",
    ".sh",
    ".vbs",
    ".msi",
    ".scr",
    ".sys",
}
ALLOWED_DIRS = {
    "core",
    "ai",
    "bot",
    "fb",
    "docs",
    "tests",
}
AI
 │
 ├── CREATE ──────→ ai/
 │                    bot/
 │                    fb/
 │                    docs/
 │
 ├── MODIFY ──────→ 已明確授權的檔案
 │
 ├── READ ────────→ 使用者明確指定的檔案
 │
 └── DENY ─────────→ 密碼
                      Token
                      Cookie
                      Session
                      私人資料
                      未授權 Core
OPER-PY3
│
├── README.md
├── INSTALL.py
├── main.py
├── requirements.txt
├── .gitignore
│
├── core/
├── ai/
├── bot/
├── fb/
├── data/
├── logs/
│
├── docs/
│   ├── ARCHITECTURE.md
│   ├── CONTEXT_POLICY.md
│   └── SECURITY.md
│
└── .github/
├── CONTRIBUTING.md
└── CODEOWNERS
OPER-PY3/
│
├── README.md
├── INSTALL.py
├── main.py
├── requirements.txt
├── .gitignore
│
├── core/
│   ├── init.py
│   ├── oper_core.py
│   ├── config.py
│   ├── memory.py
│   └── context_guard.py
│
├── ai/
│   ├── init.py
│   ├── oper_ai.py
│   ├── prompts.py
│   └── provider.py
│
├── bot/
│   ├── init.py
│   ├── oper_bot.py
│   └── tasks.py
│
├── fb/
│   ├── init.py
│   ├── publisher.py
│   └── analytics.py
│
├── data/
│   └── memory.json
│
├── docs/
│   ├── ARCHITECTURE.md
│   ├── SECURITY.md
│   └── CONTEXT_POLICY.md
│
├── .github/
│   ├── CONTRIBUTING.md
│   └── CODEOWNERS
│
└── logs/
└── .gitkeep
檔名稱和副檔名，Ai自建修改架構

OPER-PY3/
│
├── README.md
├── INSTALL.py
├── main.py
├── requirements.txt
├── .gitignore
│
├── core/
│   ├── __init__.py
│   ├── oper_core.py
│   ├── config.py
│   ├── memory.py
│   └── context_guard.py
│
├── ai/
│   ├── __init__.py
│   ├── oper_ai.py
│   ├── prompts.py
│   └── provider.py
│
├── bot/
│   ├── __init__.py
│   ├── oper_bot.py
│   └── tasks.py
│
├── fb/
│   ├── __init__.py
│   ├── publisher.py
│   └── analytics.py
│
├── data/
│   └── memory.json
│
├── docs/
│   ├── ARCHITECTURE.md
│   ├── SECURITY.md
│   └── CONTEXT_POLICY.md
│
├── .github/
│   ├── CONTRIBUTING.md
│   └── CODEOWNERS
│
└── logs/
    └── .gitkeep
