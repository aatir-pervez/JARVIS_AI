from google import genai
import os
from dotenv import load_dotenv
from datetime import datetime

from ai.memory import add_to_memory, get_memory

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("❌ API KEY NOT FOUND")
else:
    print("✅ API KEY LOADED")

client = genai.Client(api_key=api_key)


def ask_gemini(prompt):
    today = datetime.now().strftime("%A, %d %B %Y")

    add_to_memory("User", prompt)
    context = get_memory()

    full_prompt = f"""
You are Jarvis, a smart AI assistant.

Today's date is: {today}

Conversation so far:
{context}

User: {prompt}
Jarvis:
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=full_prompt
        )

        reply = response.text.strip()

    except Exception as e:
        print("Gemini Error:", e)
        reply = "Sorry boss, I'm having trouble right now."

    add_to_memory("Jarvis", reply)

    return reply