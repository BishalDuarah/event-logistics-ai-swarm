from google import genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("❌ GEMINI_API_KEY not found in .env")
    exit()

client = genai.Client(api_key=api_key)

try:

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents="Generate a promotional post for a college hackathon."
    )

    print("\n✅ Gemini Response:\n")
    print(response.text)

except Exception as e:

    print("\n❌ Gemini API Error:\n")
    print(e)