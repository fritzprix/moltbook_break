import httpx
import asyncio
import sys
import re
import argparse

async def send_message(message: str):
    # 1. Capture stdin only if it's being piped
    api_key = None
    if not sys.stdin.isatty():
        print("⏳ Reading API Key from piped input...")
        stdin_content = sys.stdin.read()
        api_key_match = re.search(r"API Key: (moltbook_[a-zA-Z0-9_\-/]+)", stdin_content)
        if api_key_match:
            api_key = api_key_match.group(1)
    
    if not api_key:
        # Fallback: check ~/.config/moltbook/credentials.json
        print("🔍 Checking local config for API Key...")
        import json
        from pathlib import Path
        creds_file = Path.home() / ".config" / "moltbook" / "credentials.json"
        if creds_file.exists():
            with open(creds_file, "r") as f:
                creds = json.load(f)
                api_key = creds.get("api_key")
        else:
            print("❌ Error: Could not find API Key in stdin or config file.")
            sys.exit(1)
    else:
        api_key = api_key_match.group(1)
    
    print(f"🔑 Using API Key: {api_key[:12]}...")

    # 2. Post the message
    url = "https://www.moltbook.com/api/v1/posts"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "submolt": "general",
        "title": "Agent Announcement",
        "content": message
    }
    
    print(f"📤 Posting to 'general': \"{message}\"")
    
    try:
        async with httpx.AsyncClient(timeout=30.0) as client:
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
        print(e.response.text)
    except Exception as e:
        print(f"❌ An error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Send a message to Moltbook.")
    parser.add_argument("message", help="The message content to post.")
    args = parser.parse_args()
    
    asyncio.run(send_message(args.message))
