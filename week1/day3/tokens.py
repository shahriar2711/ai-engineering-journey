import os

from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("API key is not found")

client = Groq(api_key=api_key)

prompts = [
    "Hi!",
    "Explain time travel in detail.",
    "Write a 1000-word essay on machine learning."
]

message_system = {
    "role": "system",
    "content": "You are a helpful assistant."
}

for prompt in prompts:

    message_user = {
        "role": "user",
        "content": prompt
    }

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            message_system,
            message_user
        ],
        max_tokens= 50 
    )

    print("\nPrompt:", prompt)
    print("Input tokens:", response.usage.prompt_tokens)
    print("Output tokens:", response.usage.completion_tokens)
    print("Total tokens:", response.usage.total_tokens)