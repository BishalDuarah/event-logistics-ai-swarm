from agents.scheduler_agent import run_scheduler_agent
from agents.scheduler_agent import parse_schedule
from agents.scheduler_agent import detect_and_resolve_conflicts

event_details = """
AI Hackathon
200 participants
3 workshops
2 guest speakers
"""

schedule_text = run_scheduler_agent(event_details)

print("Generated Schedule:")
print(schedule_text)

schedule = parse_schedule(schedule_text)

fixed_schedule = detect_and_resolve_conflicts(schedule)

print("\nFinal Schedule:")

for s in fixed_schedule:
    print(s)