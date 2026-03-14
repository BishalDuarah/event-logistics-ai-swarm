from llm import generate_text


def analyze_event(event_name, audience, platform):

    prompt = f"""
You are an AI event analytics expert.

Event: {event_name}
Audience: {audience}
Platform: {platform}

Predict:

1. Best posting time for social media
2. Expected engagement level
3. Suggested promotion strategy

Return a short analysis.
"""

    try:

        analysis = generate_text(prompt)

        return analysis

    except Exception as e:

        print("Analytics Agent Error:", e)

        return """
Best Posting Time: 6 PM
Expected Engagement: High
Strategy: Use reels, countdown posts, and speaker announcements.
"""