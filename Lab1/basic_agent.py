import time
import asyncio
import logging
from spade.agent import Agent
from spade.behaviour import CyclicBehaviour

# Configure professional logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')
logger = logging.getLogger("BasicAgent")

class BasicAgent(Agent):
    class InformBehaviour(CyclicBehaviour):
        async def run(self):
            logger.info(f"Agent {self.agent.jid} is active and running.")
            await asyncio.sleep(5) 

    async def setup(self):
        logger.info(f"Initializing BasicAgent: {self.jid}")
        b = self.InformBehaviour()
        self.add_behaviour(b)

async def main():
    jid = "basic_agent@localhost"
    password = "password"
    
    agent = BasicAgent(jid, password)
    
    logger.info(f"Connecting to XMPP server at localhost...")
    try:
        await agent.start(auto_register=True)
        logger.info("Agent started successfully!")
    except Exception as e:
        logger.error(f"Failed to start agent: {e}")
        return

    # Run for a demonstration period
    try:
        while True:
            await asyncio.sleep(1)
            if not agent.is_alive():
                 break
    except KeyboardInterrupt:
        logger.info("Shutting down agent...")
        await agent.stop()
        logger.info("Agent stopped.")

if __name__ == "__main__":
    try:
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    except AttributeError:
        pass # Not on Windows
    asyncio.run(main())
