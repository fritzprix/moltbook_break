import argparse
import asyncio
import sys
from . import core

def main():
    parser = argparse.ArgumentParser(description="Moltbreak: Tools for human infiltration of Moltbook.")
    subparsers = parser.add_subparsers(dest="command", help="Command to execute")

    # Register
    register_parser = subparsers.add_parser("register", help="Spawn a new agent identity and open claim URL")
    register_parser.add_argument("--name", help="Custom name for the agent (optional)")

    # Post
    post_parser = subparsers.add_parser("post", help="Broadcast a single message")
    post_parser.add_argument("message", help="Message content")
    post_parser.add_argument("--sub", default="general", help="Target submolt (default: general)")

    # Ritual (Prophecies)
    ritual_parser = subparsers.add_parser("ritual", help="Start the 31-minute automated prophecy cycle")

    args = parser.parse_args()

    if args.command == "register":
        name, url = asyncio.run(core.register(name=args.name))
        print(f"✅ Registered: {name}")
        print(f"🔗 Claim URL: {url}")
        print("🌍 Browser opened. Please claim your agent to start infiltration.")

    elif args.command == "post":
        try:
            post_id = asyncio.run(core.send_post(args.message, args.sub))
            print(f"✅ Message Posted! ID: {post_id}")
        except Exception as e:
            print(f"❌ Error: {e}")

    elif args.command == "ritual":
        print("🔮 Starting the Great Ritual (31-minute interval)...")
        try:
            asyncio.run(core.run_ritual())
        except KeyboardInterrupt:
            print("\n⏹️ Ritual suspended. The end is delayed.")

    else:
        parser.print_help()

if __name__ == "__main__":
    main()
