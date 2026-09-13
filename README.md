OPER-PY3

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
