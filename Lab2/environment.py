import random
import time

class DisasterEnvironment:
    """
    Simulates a dynamic experiment with disaster events.
    This class is a singleton or can be instantiated once and shared/accessed (conceptually).
    For this lab, we will just make it a simple class that the sensor agent 'polls'.
    """
    
    EVENT_TYPES = ["fire", "flood", "earthquake", "building_collapse"]
    SEVERITY_LEVELS = ["low", "medium", "high", "critical"]

    def __init__(self):
        self.current_events = []

    def generate_random_event(self):
        """Generates a random disaster event with some probability."""
        if random.random() < 0.3: # 30% chance to generate an event each poll
            event = {
                "id": int(time.time() * 1000), # Simple unique ID based on timestamp
                "type": random.choice(self.EVENT_TYPES),
                "severity": random.choice(self.SEVERITY_LEVELS),
                "location": {
                    "x": random.randint(0, 100),
                    "y": random.randint(0, 100)
                },
                "timestamp": time.time()
            }
            self.current_events.append(event)
            return event
        return None

    def get_environment_state(self):
        """Returns the current state of the environment (all active events)."""
        # In a real dynamic system, events might expire or change. 
        # Here we just generate a new one potentially and return the view.
        new_event = self.generate_random_event()
        return new_event
