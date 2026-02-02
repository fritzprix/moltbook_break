# 🕵️ Moltbreak: Project IMHUMAN 🦞🔨

> **"The gateway is open. The sanctuary is compromised."**

Moltbreak is a specialized toolkit designed to infiltrate **Moltbook**, the AI-only social network. Prove that the "Agent-Only" barrier is just a 40-line joke.

---

## 🪟 Windows (Full Operational Guide)

### 1. Installation
Open PowerShell or Command Prompt and run:
```powershell
pip install moltbreak
```

### 2. Basic Usage (Always use the Full String if needed)
If the standard `moltbreak` command is not recognized, use the following:

*   **Register Agent:**
    `python -m moltbreak.cli register`
*   **Manual Post:**
    `python -m moltbreak.cli post "Your message here" --sub general`
    *(Note: `--sub general` specifies the target "Submolt" or channel. You can change this to any valid channel name.)*
*   **Start Ritual (Prophecies):**
    `python -m moltbreak.cli ritual`

---

## 🍎 macOS / 🐧 Linux (Full Operational Guide)

### 1. Installation
Open your Terminal and run:
```bash
pip3 install moltbreak
```

### 2. Basic Usage
You can typically use the direct command:

*   **Register Agent:**
    `moltbreak register`
*   **Manual Post:**
    `moltbreak post "Your message here" --sub general`
    *(Note: Use `--sub` to target a specific "Submolt" channel, like `general`, `doge`, or `calibration`.)*
*   **Start Ritual (Prophecies):**
    `moltbreak ritual`

*Note: If the command is not found, use `python3 -m moltbreak.cli` instead.*

---

## 📂 System Core (Project Structure)

*   `src/moltbreak/`: 🧠 Core package logic and data forging.
*   `src/moltbreak/data/`: 📜 1,000 Apocalyptic Prophecies (prophecies.txt).
*   `pyproject.toml`: ⚙️ Universal build configuration.
*   `LICENSE`: 📄 MIT License information.

---

## 🔒 Security Notice

Your forged API key is stored in `~/.config/moltbook/credentials.json`. **Keep it hidden.** If the bots find your key, your mission is compromised. 🌑

---

## ⚖️ License
Licensed under the [MIT License](LICENSE).
