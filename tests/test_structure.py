OPER-PY3/
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
├── tests/
│   ├── test_core.py
│   ├── test_guard.py
│   └── test_structure.py
│
├── .github/
│   ├── CONTRIBUTING.md
│   └── CODEOWNERS
│
└── logs/
    └── .gitkeep
  
✓ 所有必要資料夾存在
✓ 所有必要檔案存在
✓ 禁止檔案不存在
✓ Python 模組可以 import
✓ JSON 可以解析
✓ Context Guard 可以運作
✓ Core / AI / Bot 可以啟動
✓ 結構完整
  允許：
.py
.md
.txt
.json
.yaml
.yml
.toml

禁止 AI 建立：
.exe
.dll
.bat
.cmd
.ps1
.sh
.vbs
.msi
.scr
.sys
  需要新檔案
   ↓
檢查 ARCHITECTURE.md
   ↓
已列出 → 可以建立
未列出 → 停止
   ↓
等待操作者批准
  
