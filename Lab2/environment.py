import random
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')
logger = logging.getLogger("DisasterEnvironment")

class DisasterEnvironment:
    """
    Simulates a dynamic disaster environment with various event types and severities.
    """
    
    EVENT_TYPES = ["fire", "flood", "earthquake", "building_collapse"]
    SEVERITY_LEVELS = ["low", "medium", "high", "critical"]

    def __init__(self):
        self.current_events = []
        logger.info("Disaster Environment initialized.")

    def generate_random_event(self):
        """Generates a random disaster event with professional logging."""
        if random.random() < 0.4: # Increased probability for better simulation
            event = {
                "id": int(time.time() * 1000),
                "type": random.choice(self.EVENT_TYPES),
                "severity": random.choice(self.SEVERITY_LEVELS),
                "location": {
                    "x": random.randint(0, 100),
                    "y": random.randint(0, 100)
                },
                "timestamp": time.time()
            }
            self.current_events.append(event)
            logger.info(f"New event generated: {event['type'].upper()} ({event['severity']}) at {event['location']}")
            return event
        return None

    def get_environment_state(self):
        """Returns the current state of the environment."""
        new_event = self.generate_random_event()
        return new_event
