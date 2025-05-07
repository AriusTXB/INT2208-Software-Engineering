import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

async def summarize_text(content: str):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": f"Summarize: {content}"}]
    )
    return response.choices[0].message.content
