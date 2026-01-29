# Lab 2: Perception and Environment Modeling

## Objective
To implement agent perception of environmental and disaster-related events.

## Components Implemented

1.  **DisasterEnvironment (`environment.py`)**:
    *   Simulates a dynamic world.
    *   Generates random disaster events (fire, flood, earthquake, building collapse) with varied severity levels.
    *   Provides an interface (`get_environment_state`) for agents to poll for updates.

2.  **SensorAgent (`sensor_agent.py`)**:
    *   Inherits from `spade.agent.Agent`.
    *   Uses a `PeriodicBehaviour` to actively "sense" or poll the environment at fixed intervals (every 3 seconds).
    *   When an event is detected, it logs the event details to the console and appends it to `event_log.txt`.

## How to Run

1.  Ensure the XMPP server is running.
2.  Navigate to the `Lab2` directory.
3.  Run the sensor agent:
    ```bash
    python sensor_agent.py
    ```
4.  Observe the console output to see the agent detecting events.
5.  Check `event_log.txt` generated in the directory to see the persistent log of sensed events.

## Percepts
The agent perceives the following attributes of a disaster event:
*   **Type**: Category of disaster (e.g., 'fire').
*   **Severity**: Criticality level (low, medium, high, critical).
*   **Location**: Coordinates (x, y) of the event.
*   **Timestamp**: When the event occurred.
