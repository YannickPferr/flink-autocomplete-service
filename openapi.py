import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
    model="code-davinci-002",
    prompt="\"\"\"\nHow to create a TABLE with Flink SQL?\n\"\"\"",
    temperature=0,
    max_tokens=64,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)

print(response)
