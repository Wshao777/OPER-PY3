OPER Context Policy

Purpose

This policy defines what information OPER AI may and may not receive.

Default Rule

No implicit context.

OPER AI must not automatically inspect or ingest the entire project.

AI receives only explicitly provided input.

Allowed

The following may be provided when explicitly requested:

- user-entered text
- selected document
- selected code file
- selected project data
- generated task input
- approved public information

Forbidden by Default

OPER must not automatically collect:

- OPER Core source code
- private files
- passwords
- API keys
- access tokens
- browser cookies
- browser sessions
- personal account information
- unrelated repository files
- hidden configuration
- environment secrets

Core Protection

The AI layer must be treated as an external processing component.

OPER Core
    |
    | explicit input only
    v
OPER AI

Not:

OPER Core
    |
    | automatic full access
    v
AI

Repository Boundary

The presence of a file inside the repository does not automatically authorize AI access to that file.

Access must be explicitly requested by the user or by an authorized local task.

Credentials

Credentials must never be embedded in source files.

Do not commit:

.env
*.token
*.key
*.secret
cookies
session files

Logging

Logs must not contain passwords, tokens, cookies or private authentication material.

Principle

Connection does not mean ownership.

Integration does not mean Core access.

AI assistance does not mean Core disclosure.
