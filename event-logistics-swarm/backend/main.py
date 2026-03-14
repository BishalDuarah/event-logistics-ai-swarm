from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from orchestrator import run_event_swarm


app = FastAPI()


# CORS (for React frontend)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class EventRequest(BaseModel):
    event_name: str
    audience: str
    platform: str
    event_details: str


@app.post("/run-swarm")
def run_swarm(data: EventRequest):

    result = run_event_swarm(
        data.event_name,
        data.audience,
        data.platform,
        data.event_details,
        "../data/participants.csv"
    )

    # IMPORTANT: return full result
    return result