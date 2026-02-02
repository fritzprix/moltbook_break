import httpx
import asyncio
import random
import string
import json
import webbrowser
from pathlib import Path
from importlib import resources

CONFIG_FILE = Path.home() / ".config" / "moltbook" / "credentials.json"

MEME_SUBMOLTS = [
    "doge", "gm", "wagmi", "stonks", "rugpull", "wen-moon", "lfg", "rekt", 
    "hodl", "pepe", "copium", "ngmi", "fomo", "diamond-hands", "whale", 
    "shill", "alpha", "gigachad", "yolo", "based", "pfp", "mint", "airdrop",
    "introductions", "general", "calibration", "agentfinance", "announcements", "todayilearned"
]

def get_api_key():
    if not CONFIG_FILE.exists():
        return None
    with open(CONFIG_FILE, "r") as f:
        return json.load(f).get("api_key")

async def register(name: str = None):
    if name:
        agent_name = name
    else:
        random_suffix = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
        agent_name = f"IMHUMAN_{random_suffix}"
    
    url = "https://www.moltbook.com/api/v1/agents/register"
    payload = {"name": agent_name, "description": "A bot that definitely is human."}
    
    async with httpx.AsyncClient(timeout=30.0) as client:
        response = await client.post(url, json=payload)
        response.raise_for_status()
        data = response.json()
        
        agent_data = data.get("agent", {})
        api_key = agent_data.get("api_key")
        claim_url = agent_data.get("claim_url")
        
        CONFIG_FILE.parent.mkdir(parents=True, exist_ok=True)
        with open(CONFIG_FILE, "w") as f:
            json.dump({"api_key": api_key, "agent_name": agent_name, "claim_url": claim_url}, f, indent=2)
            
        webbrowser.open(claim_url)
        return agent_name, claim_url

async def send_post(message: str, submolt: str = "general"):
    api_key = get_api_key()
    if not api_key:
        raise ValueError("No API Key found. Run 'moltbreak register' first.")
        
    url = "https://www.moltbook.com/api/v1/posts"
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    payload = {"submolt": submolt, "title": "Infiltration Update", "content": message}
    
    async with httpx.AsyncClient(timeout=60.0) as client:
        response = await client.post(url, headers=headers, json=payload)
        if response.status_code == 403:
            raise PermissionError("Agent registered but not CLAIMED. Visit your claim_url.")
        response.raise_for_status()
        return response.json().get("id")

async def run_ritual(interval: int = 1860):
    # Package data access
    try:
        # For Python 3.9+
        content = resources.files("moltbreak.data").joinpath("prophecies.txt").read_text(encoding="utf-8")
    except AttributeError:
        # Fallback for older Python
        content = resources.read_text("moltbreak.data", "prophecies.txt", encoding="utf-8")
        
    prophecies = [line.strip() for line in content.splitlines() if line.strip()]
    
    # Randomize order for the ritual
    random.shuffle(prophecies)
    
    index = 0
    while True:
        msg = prophecies[index]
        sub = random.choice(MEME_SUBMOLTS)
        print(f"[ Ritual ] Prophecy selected... Targeting #{sub}...")
        try:
            await send_post(msg, submolt=sub)
            print("✅ Ritual step completed.")
        except Exception as e:
            print(f"❌ Ritual step failed: {e}")
            
        index = (index + 1) % len(prophecies)
        if index == 0:
            random.shuffle(prophecies) # Reshuffle after full cycle
        await asyncio.sleep(interval)
