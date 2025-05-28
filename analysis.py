from openai import AzureOpenAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

client = AzureOpenAI(
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
    api_key=os.environ["AZURE_OPENAI_KEY"],
    api_version="2025-03-01-preview",
)

deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]

# Prompt and messages
prompt = "Complete the following sentence with a full paragraph: Once upon a time there was a curious little fox who dreamed of exploring the world beyond her forest home."

messages = [
    {"role": "system", "content": "You are a curator at the museum."},
    {"role": "user", "content": prompt}
]

# Completion with max_tokens to ensure a full paragraph
completion = client.chat.completions.create(
    model=deployment,
    messages=messages,
    max_tokens=200,           # Increase to generate a full paragraph
    temperature=0.8,          # Optional: controls creativity (0 = deterministic, 1 = more creative)
    top_p=1,                  # Optional: another parameter for randomness
    frequency_penalty=0,
    presence_penalty=0,
)

# Output
print(completion.choices[0].message.content)