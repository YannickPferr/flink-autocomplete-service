import openai
import secrets_config
import config

openai.api_key = secrets_config.openapikey

def autocomplete_with_gpt(query: str) -> list:
    url = "https://api.openai.com/v1/engines/davinci/completions"

    """ response = openai.Completion.create(
        model=config.gpt_model,
        prompt=f"{query}\n\n/* Generate multiple auto completions for the previous Flink SQL */",
        temperature=0.7,
        max_tokens=config.gpt_max_tokens,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # Response
    text_response = response.choices.text """

    text_response = "\n\nSELECT order_id, item_name FROM orders WHERE\nSELECT order_id, customer_name FROM orders WHERE\nSELECT order_id, quantity FROM orders WHERE\nSELECT order_id, shipping_address FROM orders WHERE\nSELECT order_id, order_date FROM orders WHERE"

    # Removing empty strings and break line
    suggestions = list(filter(None, text_response.split("\n")))

    return suggestions


def explanation_with_gpt(query: str) -> str:
    response = openai.Completion.create(
        model=config.gpt_model,
        prompt=f"{query}\n\n/* Describe the previous Flink SQL */",
        temperature=0.7,
        max_tokens=config.gpt_max_tokens,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response.choices[0].text
