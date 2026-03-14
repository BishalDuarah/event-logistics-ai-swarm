from orchestrator import run_event_swarm

event_name = "Neurathon Hackathon"

audience = "college students interested in AI"

platform = "Instagram"

event_details = """
AI Hackathon
200 participants
3 workshops
2 guest speakers
"""

csv_file = "../data/participants.csv"

run_event_swarm(
    event_name,
    audience,
    platform,
    event_details,
    csv_file
)