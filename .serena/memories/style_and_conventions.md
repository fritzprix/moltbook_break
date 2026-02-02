# Code Style and Conventions

- **Asynchronous:** The project heavily uses `asyncio` and `httpx.AsyncClient` for networking.
- **Configuration:** API keys and agent info are stored in the user's home directory (`~/.config/moltbook/credentials.json`).
- **Data Access:** Prophecies are stored in `src/moltbreak/data/prophecies.txt` and accessed via `importlib.resources`.
- **Configuration:** API keys and agent info are stored consistently in `~/.config/moltbook/credentials.json`.
- **Naming:** Agents are prefixed with `IMHUMAN_` followed by 4 random characters.
