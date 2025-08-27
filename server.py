# server.py
import os
from dotenv import load_dotenv

from starlette.applications import Starlette
from starlette.routing import Mount, Route
import uvicorn

from mcp.server.fastmcp import FastMCP

load_dotenv()
APP_PORT = int(os.getenv("APP_PORT", 8000))  # default port

# --- FastMCP setup ---
mcp_app = FastMCP(name="healthcare-mcp-server", stateless_http=True)

# -----------------------
# External API stubs
# -----------------------
async def call_risk_api(patient_data: dict) -> dict:
    score = 0.2 * patient_data.get("age", 50) + 5
    return {
        "risk_score": round(score, 2),
        "explanation": "Mock risk score based on age * 0.2 + 5",
        "raw_response": {"calculation_basis": "age"}
    }

async def call_labs_api(patient_id: str) -> dict:
    return {
        "labs": [
            {"test": "HbA1c", "value": 6.2, "unit": "%", "date": "2025-08-01"},
            {"test": "Cholesterol", "value": 190, "unit": "mg/dL", "date": "2025-07-15"}
        ]
    }

async def call_scheduler_api(patient_id: str, preferred_window: str) -> dict:
    return {
        "appointment_id": f"APT-{patient_id}-001",
        "scheduled_time": f"{preferred_window}T10:00:00",
        "confirmation": "Appointment scheduled successfully"
    }

# -----------------------
# MCP Tools
# -----------------------
@mcp_app.tool()
async def calculate_risk_score_tool(patient_data: dict):
    """
    Calculate a risk score for a patient using an external risk-scoring API.

    :param patient_data: Required: patient identifiers and relevant features
    """
    return await call_risk_api(patient_data)

@mcp_app.tool()
async def fetch_lab_results_tool(patient_id: str):
    """
    Fetch recent lab results for a patient from an external lab API.

    :param patient_id: Required: patient ID
    """
    return await call_labs_api(patient_id)

@mcp_app.tool()
async def schedule_follow_up_tool(patient_id: str, preferred_window: str):
    """
    Schedule a follow-up appointment for a patient via scheduling API.

    :param patient_id: Required: patient ID
    :param preferred_window: Required: preferred date/time window for the appointment
    """
    return await call_scheduler_api(patient_id, preferred_window)

# -----------------------
# Mount FastMCP under /
# -----------------------
async def homepage(request):
    return PlainTextResponse("Healthcare MCP Server running")

starlette_app = Starlette(
    debug=True,
    routes=[
        Route("/", homepage),
        Mount("/", app=mcp_app.streamable_http_app()),
    ],
    lifespan=lambda app: mcp_app.session_manager.run(),
)

if __name__ == "__main__":
    uvicorn.run(starlette_app, host="0.0.0.0", port=APP_PORT)