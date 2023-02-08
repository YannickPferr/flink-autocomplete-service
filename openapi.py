import os
import openai
import secrets_config
import config

openai.api_key = secrets_config.openapikey

response = openai.Completion.create(
    model=config.gpt_model,
    prompt="\"\"\"\nHow to create a TABLE with Flink SQL?\n\"\"\"",
    temperature=0,
    max_tokens=config.gpt_max_tokens,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)

print(response)
