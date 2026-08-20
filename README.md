# ⬡ SentinelX AI — Autonomous Cyber Defense Platform

> **10 AI Agents. One Intelligent Cybersecurity Workforce.**

SentinelX AI is a fully simulated, multi-agent cybersecurity platform that functions as an AI-powered Security Operations Center (SOC). Ten specialized agents collaborate in real time to detect, analyze, respond to, and report cyber threats — autonomously.

---

## Screenshots

| Dashboard | Agents | Threats |
|-----------|--------|---------|
| Live KPI cards, threat timeline, agent feed | 10 agent cards with confidence scores | Full event table with severity badges |

| Incidents | Compliance | Reports |
|-----------|------------|---------|
| Lifecycle: detection → resolved | ISO 27001, GDPR, NIST radar chart | Risk score gauge + executive summary |

---

## Tech Stack

### Frontend
| Tool | Purpose |
|------|---------|
| React 18 + Vite | UI framework + dev server |
| TypeScript | Type safety |
| Zustand | Global state management |
| Recharts | Charts (area, bar, line, radar) |
| React Router v6 | Client-side routing |
| Lucide React | Icons |
| Vanilla CSS | Dark cyberpunk theme with CSS variables |

### Backend
| Tool | Purpose |
|------|---------|
| Python 3.13 | Runtime |
| FastAPI | REST API + WebSocket server |
| Uvicorn | ASGI server |
| Pydantic v2 | Data validation and schemas |
| asyncio | Concurrent agent execution |

---

## Project Structure

```
sentinelx/
├── main.py                        # FastAPI app entry point
├── requirements.txt               # Python dependencies
│
├── core/
│   ├── base_agent.py              # Abstract base class for all agents
│   ├── message_bus.py             # Async pub/sub message bus + AgentMessage schema
│   └── orchestrator.py            # Initializes and runs all 10 agents concurrently
│
├── agents/
│   ├── threat_detection.py        # Agent 1 — Detects IPs, ports, intrusion patterns
│   ├── malware_analysis.py        # Agent 2 — Classifies malicious files by hash/type
│   ├── network_monitoring.py      # Agent 3 — DDoS, lateral movement, C2 beacons
│   ├── phishing_investigation.py  # Agent 4 — Phishing emails, malicious URLs
│   ├── insider_threat.py          # Agent 5 — Risky employee behavior detection
│   ├── vulnerability_scanner.py   # Agent 6 — CVEs, misconfigs, outdated software
│   ├── incident_response.py       # Agent 7 — Auto-isolation and remediation actions
│   ├── digital_forensics.py       # Agent 8 — Attack timeline reconstruction
│   ├── compliance_audit.py        # Agent 9 — ISO 27001, GDPR, NIST gap monitoring
│   └── executive_report.py        # Agent 10 — Risk scores and executive summaries
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
        ├── index.css              # Global dark cyberpunk theme
        ├── types/index.ts         # TypeScript interfaces
        ├── store/index.ts         # Zustand store (messages, agents, KPI)
        ├── hooks/
        │   └── useWebSocket.ts    # WebSocket connection + agent polling
        ├── components/
        │   ├── Sidebar.tsx        # Navigation sidebar with live status dot
        │   └── Topbar.tsx         # Page header with live threat ticker
        └── pages/
            ├── Dashboard.tsx      # KPI cards, timeline chart, live feed
            ├── Agents.tsx         # All 10 agent cards with confidence scores
            ├── Threats.tsx        # Full threat event table
            ├── Incidents.tsx      # Incident lifecycle tracker
            ├── Network.tsx        # Traffic anomaly charts + subnet load
            ├── Compliance.tsx     # Framework scores + radar chart
            ├── Reports.tsx        # Executive risk gauge + recommendations
            └── Settings.tsx       # Agent config + connection settings
```

---

## Getting Started

### Prerequisites
- Python 3.11+
- Node.js 18+
- npm 9+

### 1. Clone / navigate to the project

```bash
cd sentinelx
```

### 2. Start the Backend

```bash
# Install Python dependencies (already installed if you ran setup)
pip install -r requirements.txt

# Start the FastAPI server
uvicorn main:app --reload --port 8000
```

Backend runs at: `http://localhost:8000`
API docs at: `http://localhost:8000/docs`

### 3. Start the Frontend

```bash
cd frontend
npm install       # first time only
npm run dev
```

Frontend runs at: `http://localhost:5173`

---

## Pages & Features

### Dashboard
- 4 KPI cards — Total Events, Critical, High, Medium (live counters)
- Area chart — Threat activity timeline by severity
- Bar chart — Event distribution across all 10 agents
- Live threat feed — Real-time scrolling event stream
- Agent status panel — All agents with event counts

### Agents
- Cards for all 10 agents with icon, description, color coding
- Live event count + confidence score (%)
- Progress bar showing agent activity level
- Last detected event type per agent

### Threats
- Severity summary cards (critical / high / medium / low)
- Full sortable table of all events across all agents
- Columns: Time, Agent, Event Type, Detail, Severity

### Incidents
- Lifecycle stage counters: Detection → Analysis → Response → Resolved
- Table of all high/critical events mapped to incident IDs (INC-0001...)
- Stage and severity badges per incident

### Network
- Anomaly score + traffic line chart over time
- Subnet traffic load bars (5 subnets, color-coded by load)
- Network-specific event table with interface info

### Compliance
- Score cards for: ISO 27001, GDPR, NIST CSF, SOC 2, PCI-DSS, HIPAA
- Color-coded: green (≥85%) / yellow (≥70%) / red (<70%)
- Radar chart showing compliance posture across all frameworks
- Violations log from ComplianceAuditAgent

### Reports
- Circular risk score gauge (0–100) with color-coded risk level
- Executive recommendation text (AI-generated based on live data)
- Top 5 most active agents leaderboard
- Performance metrics: Threat Coverage, Response Rate, Detection Speed
- Full event breakdown by severity

### Settings
- Agent configuration table (name, scan interval, status)
- Notification threshold display
- Connection info (backend URL, WebSocket endpoint, version)

---

## 10 AI Agents

| # | Agent | Scan Mode | Key Output |
|---|-------|-----------|------------|
| 1 | Threat Detection | Periodic (4–8s) | Brute force, SQL injection, port scans, privilege escalation |
| 2 | Malware Analysis | Periodic (6–12s) | File hash, malware type (Ransomware, Trojan, Rootkit...) |
| 3 | Network Monitoring | Periodic (3–7s) | DDoS spikes, lateral movement, C2 beacons, bandwidth anomalies |
| 4 | Phishing Investigation | Periodic (5–10s) | Phishing emails, malicious URLs, credential harvesting sites |
| 5 | Insider Threat | Periodic (7–14s) | Mass downloads, off-hours access, policy violations |
| 6 | Vulnerability Scanner | Periodic (8–15s) | CVEs with CVSS scores, misconfigs, open ports |
| 7 | Incident Response | Reactive | Auto-isolation, firewall rules, credential revocation |
| 8 | Digital Forensics | Reactive | Attack timelines, APT attribution, persistence mechanisms |
| 9 | Compliance & Audit | Periodic (10–20s) | Framework control pass/fail, violation logging |
| 10 | Executive Report | Periodic (30s) | Risk score (0–100), risk level, recommendations |

**Reactive agents** (7 & 8) trigger only when high/critical severity events are broadcast by other agents.

---

## Architecture

```
┌─────────────────────────────────────────────────────┐
│                   React Frontend                     │
│  Dashboard │ Agents │ Threats │ Incidents │ ...      │
│                  Zustand Store                       │
│            WebSocket + REST (fetch)                  │
└──────────────────────┬──────────────────────────────┘
                       │ ws://localhost:8000/ws
                       │ GET /api/agents
                       │ GET /api/findings
┌──────────────────────▼──────────────────────────────┐
│                  FastAPI Backend                     │
│              WebSocket Broadcast Loop                │
│                  Message Bus                         │
│  ┌──────────────────────────────────────────────┐   │
│  │              Agent Orchestrator              │   │
│  │  Agent1  Agent2  Agent3  ...  Agent10        │   │
│  │     └──────────── asyncio.gather ───────┘   │   │
│  └──────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────┘
```

### Message Bus
All agents communicate through a shared async pub/sub `MessageBus`. Each agent subscribes to a named queue. Broadcasting a message (no `target_agent`) delivers it to all subscribers — enabling reactive agents to respond to other agents' findings.

### AgentMessage Schema
```python
{
  "id": "uuid",
  "source_agent": "ThreatDetectionAgent",
  "target_agent": null,          # null = broadcast
  "event_type": "brute_force_detected",
  "payload": { "detail": "...", "source": "IDS/IPS" },
  "severity": "high",            # low | medium | high | critical
  "timestamp": "2024-01-01T00:00:00"
}
```

---

## API Reference

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/agents` | All agent statuses and event counts |
| `GET` | `/api/findings` | Last 100 findings across all agents |
| `WS` | `/ws` | Real-time event stream (JSON AgentMessage) |
| `GET` | `/docs` | FastAPI Swagger UI |

---

## Disclaimer

> SentinelX AI is a **fully simulated demo platform**. All AI agents generate realistic synthetic cybersecurity data. No real network scanning, malware execution, or system access occurs. This platform is built for demonstration, education, and portfolio purposes only.

---

## License

MIT — free to use, modify, and distribute.
