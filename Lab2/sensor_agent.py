import time
import asyncio
from spade.agent import Agent
from spade.behaviour import PeriodicBehaviour
from environment import DisasterEnvironment

# Ensure you have your XMPP server running and this user is registered if needed.

class SensorAgent(Agent):
    def __init__(self, jid, password, environment):
        super().__init__(jid, password)
        self.environment = environment

    class SensingBehaviour(PeriodicBehaviour):
        async def run(self):
            # Sense the environment
            event = self.agent.environment.get_environment_state()
            
            if event:
                print(f"[{self.agent.jid}] [SENSE] Detected event: {event['type'].upper()} "
                      f"Severity: {event['severity']} at ({event['location']['x']}, {event['location']['y']})")
                # Here we could log to a file or send a message to another agent
                with open("event_log.txt", "a") as f:
                     f.write(f"[{time.ctime(event['timestamp'])}] TYPE:{event['type']} SEVERITY:{event['severity']} LOC:{event['location']}\n")
            else:
                print(f"[{self.agent.jid}] [SENSE] No new events detected.")

    async def setup(self):
        print("SensorAgent starting . . .")
        # Check environment every 3 seconds
        b = self.SensingBehaviour(period=3)
        self.add_behaviour(b)

async def main():
    jid = "sensor_agent@localhost"
    password = "password"
    
    # Initialize the environment simulation
    environment = DisasterEnvironment()
    
    agent = SensorAgent(jid, password, environment)
    
    print(f"Connecting to {jid}...")
    await agent.start()
    print("Agent started! Monitoring environment...")

    try:
        while True:
            await asyncio.sleep(1)
            if not agent.is_alive():
                break
    except KeyboardInterrupt:
        print("Stopping agent...")
        await agent.stop()

if __name__ == "__main__":
    asyncio.run(main())
