import openai
from config.settings import OPENAI_API_KEY
from config.prompts import GENERAL_SERVICE_PROMPT

openai.api_key = OPENAI_API_KEY

def handle_general_query(query: str) -> str:
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant at an e-commerce company."},
                {"role": "user", "content": GENERAL_SERVICE_PROMPT.format(query=query)}
            ],
            max_tokens=150,
            temperature=0.5
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"I'm sorry, but I encountered an error: {e}"