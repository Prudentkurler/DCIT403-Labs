# DCIT 403: Designing Intelligent Agent
## University of Ghana - Computer Science Department
### Lab Manual: Disaster Response & Relief Coordination System

---

## 🚀 Overview
This repository contains the practical implementations for **DCIT 403**. The primary project is a **Disaster Response & Relief Coordination System** built using Python and the **SPADE** (Smart Python Agent Development Environment) framework.

---

## 📂 Repository Structure

```text
.
├── Lab1/                   # Environment & Agent Platform Setup
│   ├── basic_agent.py      # Entry point for the first SPADE agent
│   └── generate_report.py  # Automated Lab 1 report generator (.docx)
├── Lab2/                   # Perception & Environment Modeling
│   ├── environment.py      # Disaster simulation world
│   ├── sensor_agent.py     # Agent that monitors the environment
│   ├── simulate.py         # Standalone simulation script
│   └── generate_report.py  # Automated Lab 2 report generator (.docx)
├── docker-compose.yml      # Local XMPP Server (Prosody) configuration
├── requirements.txt        # Python dependency list
└── README.md               # Project documentation
```

---

## 🛠️ Setup Instructions

### 1. Prerequisites
- Python 3.9+
- Docker Desktop (for local XMPP server)

### 2. Installation
Clone the repository and install the required libraries:
```bash
git clone https://github.com/Prudentkurler/DCIT403-Labs.git
cd DCIT403-Labs
pip install -r requirements.txt
```

### 3. Start XMPP Server
Use Docker to spin up the Prosody server:
```bash
docker-compose up -d
```

---

## 🧪 Lab 1: Environment Setup
**Goal:** Verify SPADE installation and XMPP server connection.

- **Run Agent:**
  ```powershell
  python Lab1/basic_agent.py
  ```
- **Professional Report:**
  - [Lab 1 Markdown Report](file:///c:/Users/user/Desktop/work/Assignments/DCIT403-Labs/Lab1/REPORT.md)
  - Generate Word: `python Lab1/generate_report.py`

---

## 🔍 Lab 2: Perception & Modeling
**Goal:** Model agent perception of disaster events (Fire, Flood, etc.).

- **Run Sensor Agent:**
  ```powershell
  python Lab2/sensor_agent.py
  ```
- **Run Simulation (Offline):**
  This script generates events and logs them without requiring a full XMPP handshake.
  ```powershell
  python Lab2/simulate.py
  ```
- **Professional Report:**
  - [Lab 2 Markdown Report](file:///c:/Users/user/Desktop/work/Assignments/DCIT403-Labs/Lab2/REPORT.md)
  - Generate Word: `python Lab2/generate_report.py`
- **Generate Report:**
  After running the agent or simulation, generate the Word report:
  ```bash
  python Lab2/generate_report.py
  ```

---

## 📄 Academic Integrity
All implementations follow the Prometheus methodology and BDI-style reasoning principles as outlined in the university syllabus.

**Developer:** Senior Intelligent Agent Designer (AI Assisted)
**Session:** Semester 1, 2025/2026 Academic Year
