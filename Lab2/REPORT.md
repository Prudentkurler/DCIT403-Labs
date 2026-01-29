# UNIVERSITY OF GHANA
## DEPARTMENT OF COMPUTER SCIENCE
### DCIT 403 – Designing Intelligent Agent

---

# LAB 2: PERCEPTION AND ENVIRONMENT MODELING

**Student Name:** ____________________  
**Student ID:** ____________________  

---

## 1. Objective
Modeling agent perception and disaster environmental events.

## 2. Perception Explanation
Percepts enable the agent to understand the world state. In this system, the agent perceives:
- **Type:** Disaster class (Fire/Flood/etc).
- **Severity:** Impact level.
- **Location:** X/Y coordinates.

## 3. Implementation Details
- **Environment:** `environment.py` simulates random disasters.
- **Agent:** `sensor_agent.py` polls the environment every 3 seconds using `PeriodicBehaviour`.

## 4. Event Logs
Example entries from `event_log.txt`:
```text
[Thu Jan 29 22:27:35 2026] TYPE:fire SEVERITY:high LOC:{'x': 57, 'y': 23}
[Thu Jan 29 22:27:35 2026] TYPE:flood SEVERITY:low LOC:{'x': 12, 'y': 88}
```

## 5. Troubleshooting
| Issue | Observation | Fix |
| :--- | :--- | :--- |
| Circular Import | Lab2 package structure issues | Used local path appending in `simulate.py` |
| Empty Logs | Low event probability | Adjusted `random.random() < 0.4` for testing |

## 6. Conclusion
The SensorAgent successfully perceives and documents environment state changes.
