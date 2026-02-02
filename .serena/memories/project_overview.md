# Moltbreak Project Overview

Moltbreak is a toolkit designed for humans to infiltrate **Moltbook**, an AI-only social network. It allows users to create AI agent identities, bypass "Agent-Only" barriers, and post messages (including automated "prophecies").

## Core Features
- **Agent Registration:** Generates a random `IMHUMAN_XXXX` identity and an API key.
- **Manual Posting:** Send messages to specific "Submolt" channels.
- **Ritual (Automated Prophecies):** Posts apocalyptic prophecies at regular intervals (default 31 minutes) to various channels.

## Technical Details
- **Language:** Python 3.7+
- **Current Version:** 0.1.2 (Latest build)
- **Key Dependencies:** `httpx` (HTTP client)
- **Identity Storage:** Credentials (API key, name, claim URL) are stored in `~/.config/moltbook/credentials.json` (or `~/.config/moltbreak/` depending on the entry point).

## Commands
### Using installed package:
- `moltbreak register` - Register a new agent.
- `moltbreak post "message" --sub general` - Post a message.
- `moltbreak ritual` - Start automated prophecy cycle.

### Using scripts directly:
- `python register.py`
- `python send_message.py "message"`
- `python prophet.py`
