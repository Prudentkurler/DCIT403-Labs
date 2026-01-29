# Disaster Response & Relief Coordination System
**Course:** DCIT 403 – Designing Intelligent Agent  
**Department:** Computer Science, University of Ghana  
**Semester:** 1, 2025/2026 Academic Year  

## Project Overview
This project involves the design and implementation of a **Disaster Response & Relief Coordination System**. It simulates a decentralized intelligent multi-agent system where autonomous agents collaborate to handling disaster events such as floods, fires, and earthquakes. The system allows agents to detect events, allocate resources, and coordinate rescue efforts under uncertainty.

## Technologies Used
*   **Language:** Python 3.9+
*   **Framework:** SPADE (Smart Python Agent Development Environment)
*   **Communication:** XMPP (via Prosody Server)
*   **Containerization:** Docker (for local XMPP server)

---

## Lab 1: Environment and Agent Platform Setup

### Objective
To configure the Python agent development environment and deploy a basic agent.

### Implementation Details
*   **Agent Script:** `Lab1/basic_agent.py`
*   **Behavior:** The agent implements a cyclic behavior that periodically prints a status message ("Hello World! I am running") to demonstrate successful connection and execution loop.

### Setup & Execution Instructions
1.  **Dependencies**: Install Python requirements.
    ```bash
    pip install -r requirements.txt
    ```
2.  **XMPP Server**: Ensure a local XMPP server (like Prosody) is running.
    ```bash
    docker-compose up -d
    ```
3.  **Run Agent**:
    ```bash
    python Lab1/basic_agent.py
    ```
4.  **Verification**:
    *   The agent connects to `localhost` (or configured server).
    *   Output confirms the agent is running and sending periodic messages.

---

## Lab 2: Perception and Environment Modeling

### Objective
To implement agent perception of environmental and disaster-related events.

### Components Implemented
1.  **DisasterEnvironment (`Lab2/environment.py`)**:
    *   Simulates a dynamic world generating random events (fire, flood, earthquake, building collapse).
    *   Events have attributes: `type`, `severity` (low/medium/high/critical), `location` (x,y), and `timestamp`.
    *   Provides a polling interface for agents.

2.  **SensorAgent (`Lab2/sensor_agent.py`)**:
    *   A SPADE agent with a `PeriodicBehaviour` (runs every 3 seconds).
    *   **Percepts**: Polls the environment to "sense" current disaster events.
    *   **Action**: Logs detected events to the console and persists them to `Lab2/event_log.txt`.

### Execution & Results
1.  **Run the Sensor Agent**:
    ```bash
    python Lab2/sensor_agent.py
    ```
2.  **Observations**:
    *   **Console**: Displays real-time detection logs, e.g., `[SENSE] Detected event: FIRE Severity: high at (45, 12)`.
    *   **Log File**: Check `Lab2/event_log.txt` for a historical record of all sensed events.
