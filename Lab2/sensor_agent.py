import time
import asyncio
import logging
from spade.agent import Agent
from spade.behaviour import PeriodicBehaviour
from .environment import DisasterEnvironment

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')
logger = logging.getLogger("SensorAgent")

class SensorAgent(Agent):
    def __init__(self, jid, password, environment):
        super().__init__(jid, password)
        self.environment = environment

    class SensingBehaviour(PeriodicBehaviour):
        async def run(self):
            logger.info("Scanning for environmental changes...")
            event = self.agent.environment.get_environment_state()
            
            if event:
                logger.warning(f"Sensed Event Detected: {event['type'].upper()} | Severity: {event['severity']} | POS: {event['location']}")
                # Log to persistent storage
                try:
                    with open("Lab2/event_log.txt", "a") as f:
                         f.write(f"[{time.ctime(event['timestamp'])}] TYPE:{event['type']} SEVERITY:{event['severity']} LOC:{event['location']}\n")
                except FileNotFoundError:
                     # Handle path if running from root
                     with open("event_log.txt", "a") as f:
                         f.write(f"[{time.ctime(event['timestamp'])}] TYPE:{event['type']} SEVERITY:{event['severity']} LOC:{event['location']}\n")
            else:
                logger.info("Ambient monitoring: No anomalies detected.")

    async def setup(self):
        logger.info(f"SensorAgent initializing sensing loop for {self.jid}")
        b = self.SensingBehaviour(period=3)
        self.add_behaviour(b)

async def main():
    jid = "sensor_agent@localhost"
    password = "password"
    
    environment = DisasterEnvironment()
    agent = SensorAgent(jid, password, environment)
    
    logger.info(f"Connecting to XMPP server for SensorAgent...")
    try:
        # For local development, we disable TLS verification to avoid certificate issues
        await agent.start(auto_register=True)
        logger.info("SensorAgent online!")
    except Exception as e:
        logger.error(f"Failed to start SensorAgent: {e}")
        return

    try:
        while True:
            await asyncio.sleep(1)
            if not agent.is_alive():
                break
    except KeyboardInterrupt:
        logger.info("Shutting down SensorAgent...")
        await agent.stop()
        logger.info("SensorAgent offline.")

if __name__ == "__main__":
    try:
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    except AttributeError:
        pass
    asyncio.run(main())
