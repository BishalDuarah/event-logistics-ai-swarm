from llm import generate_text


def generate_campaign(event_name, audience, platform):

    prompt = f"""
You are a marketing strategist for technical events.

Event: {event_name}
Audience: {audience}
Platform: {platform}

Generate a promotional post for this event.
Make it exciting and engaging.
"""

    campaign = generate_text(prompt)

    return campaign