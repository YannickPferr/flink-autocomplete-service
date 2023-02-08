
import os
import openai
import config

openai.api_key = config.openapikey

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
