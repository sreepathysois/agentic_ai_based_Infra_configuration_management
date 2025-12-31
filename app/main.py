from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from app.graph.graph import build_graph

# -----------------------------
# FastAPI App
# -----------------------------
app = FastAPI(
    title="Infra AI Agent",
    description="LangGraph-based Agentic AI for Infrastructure Automation",
    version="1.0.0",
)

# -----------------------------
# CORS (Required for Vite / Browser)
# -----------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],          # OK for lab/dev
    allow_credentials=True,
    allow_methods=["*"],          # enables OPTIONS
    allow_headers=["*"],
)

# -----------------------------
# LangGraph
# -----------------------------
graph = build_graph()

# -----------------------------
# Request Model
# -----------------------------
class RunRequest(BaseModel):
    query: str

# -----------------------------
# Health Check
# -----------------------------
@app.get("/health")
def health():
    return {"status": "ok"}

# -----------------------------
# Main Run Endpoint
# -----------------------------
@app.post("/run")
def run(req: RunRequest):
    try:
        state = {
            "user_request": req.query,
            "intent": None,
            "plan": None,
            "playbook_yaml": None,
            "validation_errors": [],
            "dry_run_output": None,
            "execution_output": None,
            "verification_output": None,
            "approved": False,
            "status": "STARTED",
        }

        return graph.invoke(state)

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

