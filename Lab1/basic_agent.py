import time
import asyncio
from spade.agent import Agent
from spade.behaviour import CyclicBehaviour

class BasicAgent(Agent):
    class InformBehaviour(CyclicBehaviour):
        async def run(self):
            print(f"[{self.agent.jid}] Hello World! I am running.")
            await asyncio.sleep(5)  # Wait for 5 seconds before repeating

    async def setup(self):
        print("Agent starting . . .")
        b = self.InformBehaviour()
        self.add_behaviour(b)

async def main():
    # Replace with your actual XMPP server details
    # If running local prosody with docker:
    # JID: agent1@localhost
    # Password: password (you might need to register this user first depending on server config)
    
    # For this example, we assume the user will replace these credentials
    # or use a public server if preferred.
    
    jid = "basic_agent@localhost"
    password = "password"
    
    agent = BasicAgent(jid, password)
    
    print(f"Connecting to {jid}...")
    await agent.start(auto_register=True)
    print("Agent started!")

    # Run for a while loop to keep the script alive
    try:
        while True:
            await asyncio.sleep(1)
            # You can add logic here to check if agent is still alive
            if not agent.is_alive():
                 break
    except KeyboardInterrupt:
        print("Stopping agent...")
        await agent.stop()
        print("Agent stopped.")

if __name__ == "__main__":
    # Ensure asyncio uses the correct loop policy on Windows if needed (Python 3.8+)
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
