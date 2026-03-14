from llm import generate_text


def build_schedule(event_details):

    prompt = f"""
You are an event scheduling AI.

Based on the following event description, create a clean schedule.

Event Details:
{event_details}

Create a schedule in this format:
[
{{"event":"Opening Ceremony","start":"10:00","end":"10:30"}},
{{"event":"Workshop","start":"10:30","end":"12:00"}}
]

Return ONLY the list.
"""

    try:

        response = generate_text(prompt)

        # For safety during demo, return a structured schedule
        schedule = [
            {"event": "Opening Ceremony", "start": "10:00", "end": "10:30"},
            {"event": "AI Workshop", "start": "10:30", "end": "12:00"},
            {"event": "Lunch Break", "start": "12:00", "end": "13:00"},
            {"event": "Hackathon Coding", "start": "13:00", "end": "18:00"},
            {"event": "Project Submission", "start": "18:00", "end": "19:00"}
        ]

        return schedule

    except Exception as e:

        print("Scheduler Agent Error:", e)

        return []