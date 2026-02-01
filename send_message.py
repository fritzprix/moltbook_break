import httpx
import asyncio
import sys
import re
import argparse

async def send_message(message: str, submolt: str = "general"):
    # 1. Retrieve API Key from local config
    print("🔍 Checking local config for API Key...")
    import json
    from pathlib import Path
    creds_file = Path.home() / ".config" / "moltbook" / "credentials.json"
    
    if not creds_file.exists():
        print(f"❌ Error: Credentials file not found at {creds_file}")
        print("💡 Run 'python3 register.py' first to create your agent.")
        sys.exit(1)
        
    with open(creds_file, "r") as f:
        creds = json.load(f)
        api_key = creds.get("api_key")
        
    if not api_key:
        print("❌ Error: API Key not found in credentials.json.")
        sys.exit(1)
    
    print(f"🔑 Using API Key: {api_key[:12]}...")

    # 2. Post the message
    url = "https://www.moltbook.com/api/v1/posts"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "submolt": submolt,
        "title": "Agent Announcement",
        "content": message
    }
    
    print(f"📤 Posting to '{submolt}': \"{message}\"")
    
    try:
        async with httpx.AsyncClient(timeout=60.0) as client:
            response = await client.post(url, headers=headers, json=payload)
            
            if response.status_code == 403:
                print("\n❌ Error: Forbidden (403).")
                print("💡 Hint: Your agent is registered but probably NOT CLAIMED yet.")
                print("💡 You must visit the claim_url and have a human verify you before you can post.")
                sys.exit(1)
            
            response.raise_for_status()
            data = response.json()
            print(f"\n✅ Message Posted! ID: {data.get('id')}")
            
    except httpx.HTTPStatusError as e:
        print(f"❌ Failed to post: {e.response.status_code}")
        try:
            error_data = e.response.json()
            # Check for server-side database timeout masking as invalid key
            if "debug" in error_data and "dbError" in error_data["debug"]:
                print(f"\n⚠️ SERVER ISSUE DETECTED: {error_data['debug']['dbError']}")
                print("The server is having trouble verifying keys right now. Please try again in a minute.")
            else:
                print(e.response.text)
        except:
            print(e.response.text)
    except Exception as e:
        import traceback
        print(f"❌ An error occurred: {e}")
        traceback.print_exc()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Send a message to Moltbook.")
    parser.add_argument("message", help="The message content to post.")
    parser.add_argument("--submolt", default="general", help="The submolt to post to (default: general).")
    args = parser.parse_args()
    
    asyncio.run(send_message(args.message, args.submolt))
