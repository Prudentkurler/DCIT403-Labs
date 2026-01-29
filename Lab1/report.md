# Lab 1: Environment and Agent Platform Setup

## Objective
To configure the Python agent development environment and deploy a basic agent.

## Setup Instructions

1.  **Environment Setup**:
    *   Clone the repository.
    *   Install dependencies: `pip install -r requirements.txt`.
    *   Ensure an XMPP server is running. A `docker-compose.yml` is provided to run Prosody locally:
        ```bash
        docker-compose up -d
        ```

2.  **Agent Execution**:
    *   Navigate to the `Lab1` directory.
    *   Update the `basic_agent.py` file with valid XMPP credentials (JID and password).
    *   Run the agent:
        ```bash
        python basic_agent.py
        ```

3.  **Output**:
    *   The agent connects to the XMPP server.
    *   It prints "Hello World! I am running." every 5 seconds.

## Code Explanation
The `BasicAgent` class inherits from `spade.agent.Agent`. It defines a `CyclicBehaviour` called `InformBehaviour`. In SPADE, a behavior represents a task that an agent can perform. A `CyclicBehaviour` repeats indefinitely. The `setup` method is overridden to add this behavior to the agent at startup.
