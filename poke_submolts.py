import httpx
import asyncio

MEME_SUBMOLTS = [
    "doge", "gm", "wagmi", "stonks", "rugpull", "wen-moon", "lfg", "rekt", 
    "hodl", "pepe", "copium", "ngmi", "fomo", "diamond-hands", "whale", 
    "shill", "alpha", "gigachad", "yolo", "based", "pfp", "mint", "airdrop",
    "introductions", "general", "calibration", "agentfinance", "announcements", "todayilearned"
]

async def poke_submolt(client, sub):
    url = f"https://www.moltbook.com/m/{sub}"
    try:
        response = await client.get(url, follow_redirects=True)
        return sub, response.status_code
    except Exception as e:
        return sub, str(e)

async def main():
    print(f"🔍 Poking {len(MEME_SUBMOLTS)} submolts on Moltbook...")
    async with httpx.AsyncClient(timeout=10.0) as client:
        tasks = [poke_submolt(client, sub) for sub in MEME_SUBMOLTS]
        results = await asyncio.gather(*tasks)
        
    print("\n--- Results ---")
    valid_subs = []
    for sub, status in results:
        status_str = f"[{status}]"
        if status == 200:
            status_str = f"✅ {status_str}"
            valid_subs.append(sub)
        else:
            status_str = f"❌ {status_str}"
        print(f"{sub:15} : {status_str}")
    
    print(f"\n✨ Total Valid Submolts Found: {len(valid_subs)}")
    print(f"Valid list: {valid_subs}")

if __name__ == "__main__":
    asyncio.run(main())
