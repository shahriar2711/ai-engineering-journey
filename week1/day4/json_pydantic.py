import os
import json

from dotenv import load_dotenv
from groq import Groq
from pydantic import BaseModel


# Load environment variables
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("API key is not found")


# Create Groq client
client = Groq(api_key=api_key)


# Pydantic model
class CustomerInformation(BaseModel):
    name: str
    device: str
    issue: str
    address: str
    email: str
    phone_number: str


# Customer ticket
text = """
Hello my name is Atiq.
I have an iPhone which is not working.
My address is Chittagong.
My email is atiq@gmail.com.
My phone number is 01829465646.
"""


# Messages
message_system = {
    "role": "system",
    "content": "You are a helpful assistant that extracts customer information."
}

message_user = {
    "role": "user",
    "content": f"""
Extract the following information from this customer ticket:

{text}

Return the information according to the provided JSON schema.
"""
}


# JSON schema
schema = CustomerInformation.model_json_schema()

# Required by Groq strict structured outputs
schema["additionalProperties"] = False


# API request
response = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[
        message_system,
        message_user
    ],
    response_format={
        "type": "json_schema",
        "json_schema": {
            "name": "customer_information",
            "strict": True,
            "schema": schema
        }
    }
)


# Get JSON string from response
raw_json = response.choices[0].message.content

print("Raw JSON:")
print(raw_json)


# Convert JSON string → Python dictionary
data = json.loads(raw_json)


# Validate dictionary using Pydantic
customer = CustomerInformation.model_validate(data)


print("\nValidated Customer Information:")
print(customer)