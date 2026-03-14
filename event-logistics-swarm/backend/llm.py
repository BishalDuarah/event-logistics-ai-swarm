from google import genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get API key
API_KEY = os.getenv("GEMINI_API_KEY")

# Initialize Gemini client
client = genai.Client(api_key=API_KEY)

# Cache last successful response (demo safety)
last_response = None


def generate_text(prompt):

    global last_response

    try:

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )

        text = response.text

        # Save response in cache
        last_response = text

        return text

    except Exception as e:

        print("Gemini API Error:", e)

        # If Gemini fails but we have a cached response
        if last_response:
            return last_response

        # Demo fallback responses
        if "marketing strategist" in prompt.lower() or "promotional" in prompt.lower():

            return """
🚀 Join the Neurathon Hackathon!

A 36-hour innovation sprint where students collaborate, build AI-powered solutions,
and compete for exciting prizes.

Whether you're a developer, designer, or AI enthusiast — this is your chance to
showcase your creativity and build something amazing.

Register now and be part of the future of innovation!
"""

        if "personalize this email" in prompt.lower() or "email" in prompt.lower():

            return """
Hello,

We are excited to have you join the Neurathon Hackathon!

Prepare for an exciting 36-hour journey of innovation, collaboration, and coding.
The event schedule will be shared soon.

Looking forward to seeing your ideas come to life!

Best regards,
Event Organizing Team
"""

        if "schedule" in prompt.lower():

            return """
10-11 Opening Ceremony
11-12 Workshop: AI Fundamentals
12-13 Keynote Speaker
13-36 Hackathon Coding Session
"""

        return "AI service temporarily unavailable. Please try again later."