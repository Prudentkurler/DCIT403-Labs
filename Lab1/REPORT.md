# UNIVERSITY OF GHANA
## DEPARTMENT OF COMPUTER SCIENCE
### DCIT 403 – Designing Intelligent Agent

---

# LAB 1: ENVIRONMENT AND AGENT PLATFORM SETUP

**Student Name:** ____________________  
**Student ID:** ____________________  

---

## 1. Introduction
This report documents the successful setup of the multi-agent development environment using SPADE and XMPP.

## 2. Environment Setup Report
The following configuration was applied:
- **Python:** 3.9+ environment.
- **Library:** SPADE (Smart Python Agent Development Environment).
- **Server:** Prosody XMPP Server running via Docker container.
- **Container status:** Configured on port 5222 using `docker-compose.yml`.

## 3. Implementation (Summary)
The `BasicAgent` was implemented to test the connection. It utilizes a `CyclicBehaviour` that remains active as long as the agent is connected.

```python
# Laboratory Verification Logic
async def setup(self):
    self.add_behaviour(self.InformBehaviour())
```

## 4. Troubleshooting
| Issue | Cause | Resolution |
| :--- | :--- | :--- |
| `pip install lxml` failed | Python 3.14 lacks pre-built wheels | Use GitHub Codespaces or install C++ Build Tools |
| Connection Refused | Docker container not running | Execute `docker-compose up -d` |
| Auth Failure | JID not registered | Enable `auto_register=True` in code |

## 5. Conclusion
The environment is functional and ready for further agent behavioral modeling.
