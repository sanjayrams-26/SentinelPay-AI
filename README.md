# 🛡️ SentinelPay AI — Autonomous AI Risk Management Platform

> **10 AI Agents. One Intelligent Risk Management Workforce.**

SentinelPay AI is a fully simulated, multi-agent AI risk management platform designed to function as an intelligent transaction and security risk operations system. Ten specialized agents collaborate in real time to detect, analyze, investigate, respond to, and report potential risks and suspicious activities autonomously.

---

## 📸 Screenshots

| **Dashboard**                             | **Agents**                            | **Threats & Risks**                   |
| ----------------------------------------- | ------------------------------------- | ------------------------------------- |
| Live KPI cards, risk timeline, agent feed | 10 agent cards with confidence scores | Full event table with severity badges |

| **Incidents**                   | **Compliance**                    | **Reports**                          |
| ------------------------------- | --------------------------------- | ------------------------------------ |
| Lifecycle: detection → resolved | ISO 27001, GDPR, NIST radar chart | Risk score gauge + executive summary |

---

# 🛠️ Tech Stack

## Frontend

| Tool            | Purpose                                        |
| --------------- | ---------------------------------------------- |
| React 18 + Vite | UI framework + development server              |
| TypeScript      | Type safety                                    |
| Zustand         | Global state management                        |
| Recharts        | Charts including area, bar, line, and radar    |
| React Router v6 | Client-side routing                            |
| Lucide React    | Icons                                          |
| Vanilla CSS     | Dark modern dashboard theme with CSS variables |

## Backend

| Tool        | Purpose                     |
| ----------- | --------------------------- |
| Python 3.13 | Runtime                     |
| FastAPI     | REST API + WebSocket server |
| Uvicorn     | ASGI server                 |
| Pydantic v2 | Data validation and schemas |
| asyncio     | Concurrent agent execution  |

---

# 📁 Project Structure

```text
sentinelpay-ai/
├── main.py                        # FastAPI app entry point
├── requirements.txt               # Python dependencies
│
├── core/
│   ├── base_agent.py              # Abstract base class for all agents
│   ├── message_bus.py             # Async pub/sub message bus + AgentMessage schema
│   └── orchestrator.py            # Initializes and runs all 10 agents concurrently
│
├── agents/
│   ├── threat_detection.py        # Agent 1 — Detects suspicious patterns and risk events
│   ├── malware_analysis.py        # Agent 2 — Classifies malicious files by hash/type
│   ├── network_monitoring.py      # Agent 3 — Detects network anomalies and unusual activity
│   ├── phishing_investigation.py  # Agent 4 — Investigates phishing emails and malicious URLs
│   ├── insider_threat.py          # Agent 5 — Detects risky user and employee behaviour
│   ├── vulnerability_scanner.py   # Agent 6 — Identifies CVEs, misconfigs, and outdated software
│   ├── incident_response.py       # Agent 7 — Handles automated response and remediation actions
│   ├── digital_forensics.py       # Agent 8 — Reconstructs incident and attack timelines
│   ├── compliance_audit.py        # Agent 9 — Monitors ISO 27001, GDPR, and NIST compliance
│   └── executive_report.py        # Agent 10 — Generates risk scores and executive summaries
│
├── api/
│   └── server.py                  # REST endpoints + WebSocket broadcast loop
│
└── frontend/
    ├── index.html
    ├── vite.config.ts
    ├── tsconfig.json
    ├── package.json
    └── src/
        ├── main.tsx               # React entry point
        ├── App.tsx                # Router + layout
        ├── index.css              # Global dark dashboard theme
        ├── types/index.ts         # TypeScript interfaces
        ├── store/index.ts         # Zustand store for messages, agents, and KPI data
        ├── hooks/
        │   └── useWebSocket.ts    # WebSocket connection + agent polling
        ├── components/
        │   ├── Sidebar.tsx        # Navigation sidebar with live status
        │   └── Topbar.tsx         # Page header with live risk ticker
        └── pages/
            ├── Dashboard.tsx      # KPI cards, timeline chart, and live feed
            ├── Agents.tsx         # All 10 agent cards with confidence scores
            ├── Threats.tsx        # Full risk and event table
            ├── Incidents.tsx      # Incident lifecycle tracker
            ├── Network.tsx        # Traffic anomaly charts + subnet load
            ├── Compliance.tsx     # Framework scores + radar chart
            ├── Reports.tsx        # Executive risk gauge + recommendations
            └── Settings.tsx       # Agent configuration + connection settings
```

---

# 🚀 Getting Started

## Prerequisites

* Python 3.11+
* Node.js 18+
* npm 9+

## 1. Clone / Navigate to the Project

```bash
cd sentinelpay-ai
```

## 2. Start the Backend

```bash
# Install Python dependencies
pip install -r requirements.txt

# Start the FastAPI server
uvicorn main:app --reload --port 8000
```

Backend runs at:

`http://localhost:8000`

API documentation:

`http://localhost:8000/docs`

## 3. Start the Frontend

```bash
cd frontend

npm install

npm run dev
```

Frontend runs at:

`http://localhost:5173`

---

# 📊 Pages & Features

## 🏠 Dashboard

* 4 KPI cards — Total Events, Critical, High, Medium
* Area chart showing risk activity timeline by severity
* Bar chart showing event distribution across all 10 agents
* Live risk and event feed
* Agent status panel with event counts

## 🤖 Agents

* Cards for all 10 AI agents
* Agent icon and description
* Live event count
* Confidence score
* Progress bar showing agent activity
* Last detected event type

## 🚨 Threats & Risks

* Severity summary cards
* Critical, High, Medium, and Low classifications
* Full sortable table of events across all agents
* Time, Agent, Event Type, Detail, and Severity information

## 🔍 Incidents

* Lifecycle stage counters:

```text
Detection → Analysis → Response → Resolved
```

* High and critical events mapped to incident IDs
* Incident format:

```text
INC-0001
INC-0002
INC-0003
```

* Stage and severity badges

## 🌐 Network

* Network anomaly score
* Traffic line chart over time
* Subnet traffic load bars
* Network-specific event table
* Interface information and anomaly indicators

## 📋 Compliance

* Score cards for:

  * ISO 27001
  * GDPR
  * NIST CSF
  * SOC 2
  * PCI-DSS
  * HIPAA

* Risk-based color classification:

```text
Green  → ≥ 85%
Yellow → ≥ 70%
Red    → < 70%
```

* Radar chart showing compliance posture
* Violations log from the Compliance Audit Agent

## 📈 Reports

* Circular risk score gauge from 0–100
* AI-generated executive recommendations
* Top 5 most active agents leaderboard
* Performance metrics:

  * Risk Coverage
  * Response Rate
  * Detection Speed
* Full event breakdown by severity

## ⚙️ Settings

* Agent configuration table
* Agent name
* Scan interval
* Agent status
* Notification threshold
* Backend connection information
* WebSocket endpoint
* Application version

---

# 🤖 10 AI Agents

| #  | Agent                  | Scan Mode         | Key Output                                                     |
| -- | ---------------------- | ----------------- | -------------------------------------------------------------- |
| 1  | Threat Detection       | Periodic (4–8s)   | Brute force, SQL injection, port scans, privilege escalation   |
| 2  | Malware Analysis       | Periodic (6–12s)  | File hash, malware type such as Ransomware, Trojan, Rootkit    |
| 3  | Network Monitoring     | Periodic (3–7s)   | DDoS spikes, lateral movement, C2 beacons, bandwidth anomalies |
| 4  | Phishing Investigation | Periodic (5–10s)  | Phishing emails, malicious URLs, credential harvesting sites   |
| 5  | Insider Threat         | Periodic (7–14s)  | Mass downloads, off-hours access, policy violations            |
| 6  | Vulnerability Scanner  | Periodic (8–15s)  | CVEs with CVSS scores, misconfigurations, open ports           |
| 7  | Incident Response      | Reactive          | Auto-isolation, firewall rules, credential revocation          |
| 8  | Digital Forensics      | Reactive          | Attack timelines, APT attribution, persistence mechanisms      |
| 9  | Compliance & Audit     | Periodic (10–20s) | Framework control pass/fail and violation logging              |
| 10 | Executive Report       | Periodic (30s)    | Risk score from 0–100, risk level, and recommendations         |

> **Reactive agents — Agent 7 and Agent 8 — are triggered when high or critical severity events are broadcast by other agents.**

---

# 🏗️ Architecture

```text
┌─────────────────────────────────────────────────────┐
│                   React Frontend                     │
│                                                     │
│  Dashboard │ Agents │ Threats │ Incidents │ ...     │
│                                                     │
│                  Zustand Store                      │
│                                                     │
│            WebSocket + REST (fetch)                 │
└──────────────────────┬──────────────────────────────┘
                       │
                       │ ws://localhost:8000/ws
                       │ GET /api/agents
                       │ GET /api/findings
                       │
┌──────────────────────▼──────────────────────────────┐
│                  FastAPI Backend                     │
│                                                     │
│              WebSocket Broadcast Loop               │
│                                                     │
│                  Message Bus                         │
│                                                     │
│  ┌──────────────────────────────────────────────┐  │
│  │              Agent Orchestrator              │  │
│  │                                              │  │
│  │ Agent1  Agent2  Agent3  ...  Agent10         │  │
│  │                                              │  │
│  │      └────── asyncio.gather ──────┘          │  │
│  └──────────────────────────────────────────────┘  │
│                                                     │
└─────────────────────────────────────────────────────┘
```

---

# 🔄 Message Bus

All 10 AI agents communicate through a shared asynchronous publish/subscribe `MessageBus`.

Each agent subscribes to a named queue. When a message is broadcast without a specific `target_agent`, the message is delivered to all subscribed agents.

This allows the reactive agents to respond automatically when other agents detect high-risk or critical events.

---

# 📨 AgentMessage Schema

```json
{
  "id": "uuid",
  "source_agent": "ThreatDetectionAgent",
  "target_agent": null,
  "event_type": "brute_force_detected",
  "payload": {
    "detail": "...",
    "source": "IDS/IPS"
  },
  "severity": "high",
  "timestamp": "2024-01-01T00:00:00"
}
```

`target_agent: null` indicates that the event is broadcast to all subscribed agents.

Severity levels:

```text
low
medium
high
critical
```

---

# 🔌 API Reference

| Method | Endpoint        | Description                                       |
| ------ | --------------- | ------------------------------------------------- |
| `GET`  | `/api/agents`   | Returns all AI agent statuses and event counts    |
| `GET`  | `/api/findings` | Returns the latest 100 findings across all agents |
| `WS`   | `/ws`           | Real-time event stream using JSON AgentMessage    |
| `GET`  | `/docs`         | FastAPI Swagger UI                                |

---

# 🔄 System Workflow

```text
                ┌─────────────────┐
                │  Incoming Event │
                └────────┬────────┘
                         │
                         ▼
              ┌──────────────────────┐
              │  Specialized Agents  │
              │  Detect & Analyze    │
              └──────────┬───────────┘
                         │
                         ▼
                 ┌───────────────┐
                 │  Message Bus  │
                 └───────┬───────┘
                         │
             ┌───────────┴───────────┐
             ▼                       ▼
    ┌────────────────┐      ┌─────────────────┐
    │ Incident Agent │      │ Forensics Agent │
    │    Response    │      │    Analysis     │
    └────────┬───────┘      └────────┬────────┘
             │                       │
             └───────────┬───────────┘
                         ▼
              ┌──────────────────────┐
              │ Executive Report AI  │
              │ Risk Score & Insights│
              └──────────┬───────────┘
                         │
                         ▼
              ┌──────────────────────┐
              │   React Dashboard    │
              │ Real-Time Monitoring │
              └──────────────────────┘
```

---

# 🎯 Key Highlights

* 🤖 **10 specialized AI agents**
* ⚡ Concurrent agent execution using `asyncio`
* 🔄 Real-time communication through WebSockets
* 📡 Shared asynchronous message bus
* 🚨 Automated incident response workflow
* 🔍 Digital forensic analysis
* 🌐 Network anomaly monitoring
* 🛡️ Threat and risk detection
* 📋 Multi-framework compliance monitoring
* 📊 Real-time analytics dashboard
* 📈 Executive risk scoring and recommendations
* 🎨 Modern React and TypeScript interface

---

# ⚠️ Disclaimer

> SentinelPay AI is a **fully simulated demonstration platform**. All AI agents generate realistic synthetic cybersecurity and risk-related data. No real network scanning, malware execution, payment processing, or unauthorized system access occurs.
>
> This project is built for **demonstration, education, research, portfolio, and AI Builder Internship purposes only**.

---

# 🔮 Future Enhancements

* Real-time payment transaction risk analysis
* Machine learning-based anomaly detection
* Advanced AI-powered risk scoring
* Integration with streaming platforms
* Historical risk analytics
* Continuous learning from reviewed incidents
* Merchant and transaction risk profiles
* Automated alert notifications
* Role-based access control
* Cloud deployment and monitoring
* Integration with external security and payment APIs

---

# 👨‍💻 Author

**Sanjay Ram S**

Full Stack Developer | AI/ML Enthusiast | Cloud Explorer

📧 **Email:** `sanjayram.s2024cse@sece.ac.in`

🐙 **GitHub:** `https://github.com/sanjayrams-26`

---

# 📄 License

MIT License

Free to use, modify, and distribute for educational and portfolio purposes.

---

<p align="center">
  <b>🛡️ SentinelPay AI — Intelligent Agents. Smarter Risk Decisions.</b>
</p>

<p align="center">
  ⭐ If you find this project interesting, consider giving it a star!
</p>
