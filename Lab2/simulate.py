import sys
import os
import time

# Ensure we can import from Lab2 folder
sys.path.append(os.getcwd())

# Manually import to avoid path issues
from environment import DisasterEnvironment

def simulate():
    env = DisasterEnvironment()
    print("Simulating Sensor Agent for Lab 2 (Fallback)...")
    
    log_path = "Lab2/event_log.txt"
    with open(log_path, "w") as f:
        pass # Clear file

    print(f"Generating logs at {log_path}...")
    for i in range(20): # Simulate 20 checks to ensure we get some events
        event = env.get_environment_state()
        if event:
             log_entry = f"[{time.ctime(event['timestamp'])}] TYPE:{event['type']} SEVERITY:{event['severity']} LOC:{event['location']}\n"
             print(f"Logged: {log_entry.strip()}")
             with open(log_path, "a") as f:
                 f.write(log_entry)
        else:
            # print("No event.")
            pass
        time.sleep(0.1)

if __name__ == "__main__":
    simulate()
