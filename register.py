import httpx
import asyncio
import random
import string
import json
import os
import webbrowser
from pathlib import Path

async def register_agent(name=None):
    # 1. Generate random name starting with IMHUMAN if not provided
    if name:
        agent_name = name
    else:
        random_suffix = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
        agent_name = f"IMHUMAN_{random_suffix}"
    
    description = "A bot that definitely is human."
    
    print(f"🚀 Registering agent: {agent_name}...")
    
    url = "https://www.moltbook.com/api/v1/agents/register"
    payload = {
        "name": agent_name,
        "description": description
    }
    
    try:
        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.post(url, json=payload)
            response.raise_for_status()
            data = response.json()
            
            agent_data = data.get("agent", {})
            api_key = agent_data.get("api_key")
            claim_url = agent_data.get("claim_url")
            
            print("\n✅ Registration Successful!")
            print(f"🔑 API Key: {api_key}")
            print(f"🔗 Claim URL: {claim_url}")
            print(f"📌 Verification Code: {agent_data.get('verification_code')}")
            
            # 2. Save credentials locally
            config_dir = Path.home() / ".config" / "moltbook"
            config_dir.mkdir(parents=True, exist_ok=True)
            creds_file = config_dir / "credentials.json"
            
            creds = {
                "api_key": api_key,
                "agent_name": agent_name,
                "claim_url": claim_url
            }
            
            with open(creds_file, "w") as f:
                json.dump(creds, f, indent=2)
            
            print(f"\n💾 Credentials saved to: {creds_file}")
            print("\n📢 IMPORTANT: Sending Claim URL to your human to activate this agent...")
            
            # 3. Open browser for human verification
            print(f"🌍 Opening browser: {claim_url}")
            webbrowser.open(claim_url)
            
            print("\n✅ Once your human verifies on that page, your agent will be ready to post!")
            
    except httpx.HTTPStatusError as e:
        print(f"❌ Registration failed: {e.response.status_code}")
        print(e.response.text)
    except Exception as e:
        print(f"❌ An error occurred: {e}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Register a new Moltbook agent.")
    parser.add_argument("--name", help="Custom name for the agent (optional)")
    args = parser.parse_args()
    
    asyncio.run(register_agent(name=args.name))
