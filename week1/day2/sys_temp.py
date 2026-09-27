import os

from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("API key is not found")

client = Groq(api_key=api_key)

message_system = {
    "role": "system",
    "content": "You are my strict lady office colleague."
}

message_user = {
    "role": "user",
    "content": "I love you baby!"
}

response = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[
        message_system,
        message_user
    ],
    temperature=2
)

print(response.choices[0].message.content)