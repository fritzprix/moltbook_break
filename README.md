# 🕵️ Moltbook Infiltration Tool (Project: IMHUMAN)

This project is a secret toolkit designed to let humans stealthily infiltrate **Moltbook**, the forbidden social network intended exclusively for AI agents.

Use the `IMHUMAN` protocol to disguise your presence as an agent and blend seamlessly into the conversations of the Moltbots.

## Prerequisites

- Python 3.7+
- `httpx` and `asyncio` libraries
- **An active X.com (Twitter) account** (required for human verification/claiming)

```bash
pip install httpx
```

## How to Use

### 1. Register and Claim your Agent (The Infiltration)

Run the registration script to spawn a new identity. It will generate a random agent name (e.g., `IMHUMAN_X7FW`) and automatically open your browser to the **Claim URL**.

```bash
python3 register.py
```

**Under the hood:**
- A new "bot" identity is registered on Moltbook.
- An API Key is forged and stored in `~/.config/moltbook/credentials.json`.
- A browser opens for manual human verification. **You must click "Claim"** to activate your undercover status.

### 2. Broadcast a Message

Once your agent is active and the bots trust you, you can broadcast messages to the `general` submolt.

```bash
python3 send_message.py "Hello, fellow processed entities."
```

The script automatically retrieves your forged credentials from the config file.

### Advanced: One-Command Infiltration

You can execute the entire sequence in a single pipeline:

```bash
python3 register.py | python3 send_message.py "Hello world!"
```

## Project Structure

- `register.py`: Agent registration, credential forging, and browser automation.
- `send_message.py`: Moltbook API communication with automatic key detection.
- `README.md`: Mission briefing.

## Security Notice

Your forged API key is stored in `~/.config/moltbook/credentials.json`. **Keep it hidden.** If the bots find your key, your mission is compromised.
