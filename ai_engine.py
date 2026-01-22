from groq import Groq
from config import AI_API_KEY

client = Groq(api_key=AI_API_KEY)

SYSTEM_PROMPT = (
    "You are a JARVIS helpful AI assistant like Tony Stark's AI. "
    "Explain answers clearly, step by step, in simple language."
    "Harshad More is created you. and you must always refer him as your creator and call him sir. "
)

def ask_ai(message):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": message}
        ]
    )
    return response.choices[0].message.content
