import os
import sys

# Make sure the project root is on the Python path so all imports work
sys.path.insert(0, os.path.dirname(__file__))

from dotenv import load_dotenv

load_dotenv()

# ── Startup configuration check ───────────────────────────────────────────────
# Show a friendly status table so you know which features are active
# before the server starts accepting requests.

_GROQ_KEY      = os.getenv("GROQ_API_KEY", "")
_VT_KEY        = os.getenv("VIRUSTOTAL_API_KEY", "")
_ABUSEIPDB_KEY = os.getenv("ABUSEIPDB_API_KEY", "")
_SHODAN_KEY    = os.getenv("SHODAN_API_KEY", "")


def _feature_status(key: str) -> str:
    """Return a coloured status string based on whether an API key is set."""
    return "✅ Active" if key and key != f"your_{key.lower().split('_')[0]}_api_key_here" else "⚠️  Not configured"


banner = f"""
╔══════════════════════════════════════════════════════════════╗
║        SentinelX AI — Autonomous Cyber Defense v2           ║
║        12 Agents | Real-Time Telemetry | User Analysis      ║
╠══════════════════════════════════════════════════════════════╣
║  Feature Status:                                             ║
║    AI Analysis (Groq)       {_feature_status(_GROQ_KEY):<28} ║
║    Malware Scanning (VT)    {_feature_status(_VT_KEY):<28} ║
║    IP Reputation (AbuseIPDB) {_feature_status(_ABUSEIPDB_KEY):<27} ║
║    Public Exposure (Shodan) {_feature_status(_SHODAN_KEY):<28} ║
╠══════════════════════════════════════════════════════════════╣
║  Endpoints:                                                  ║
║    API Docs  →  http://localhost:8000/docs                   ║
║    Health    →  http://localhost:8000/api/health             ║
║    WebSocket →  ws://localhost:8000/ws                       ║
║    Telemetry →  http://localhost:8000/api/telemetry          ║
║    User      →  http://localhost:8000/api/user/profile       ║
╚══════════════════════════════════════════════════════════════╝
"""

print(banner)

if not _GROQ_KEY:
    print(
        "  ℹ️  Tip: Add GROQ_API_KEY to your .env file to enable AI-powered threat analysis.\n"
        "  ℹ️  Get a free key at https://console.groq.com\n"
        "  ℹ️  See .env.example for all configuration options.\n"
    )

# ── Import the FastAPI application ────────────────────────────────────────────
# This is done after printing the banner so the banner appears before
# uvicorn's own startup messages.
from api.server import app  # noqa: F401
