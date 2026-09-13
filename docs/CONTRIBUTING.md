Contributing to OPER-PY3

Before Contributing

Read:

- README.md
- docs/ARCHITECTURE.md
- docs/CONTEXT_POLICY.md
- docs/SECURITY.md

Core Boundary

Contributions must not bypass the OPER Core context boundary.

Do not add code that automatically:

- reads the entire repository
- searches for credentials
- extracts browser cookies
- extracts authentication sessions
- sends private files to external AI services

AI

AI integrations must receive explicit, controlled input.

Bot

Automation should perform legitimate local tasks.

Do not add artificial traffic or fake engagement systems.

Pull Requests

Explain:

1. What changed
2. Why it changed
3. Which modules are affected
4. Whether data access changed
5. Whether external services are involved

Ownership

Contributing code does not transfer ownership of proprietary OPER Core components.

Quality

Keep modules small, documented and independently testable.
