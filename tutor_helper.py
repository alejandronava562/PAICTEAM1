from openai import OpenAI
import json
from typing import Any, Dict

from env_loader import get_openai_api_key

system_tutor = """You are tutor that helps users when they get a question wrong.
When a user gets something wrong, output a JSON with this format:
{
    "message": "You were close, but got it wrong:...",
    "explanation": "PUT EXPLANATION HERE",
    "user_answer": " : "PUT THE USER ANSWER"
    "correct_answer": "PUT CORRECT ANSWER"
}
"""


def _client():
    return OpenAI(api_key=get_openai_api_key())


def ai_tutor_reply(question: str, context: str, model="gpt-5") -> Dict[str, Any]:
    client = _client()
    response = client.chat.completions.create(
        model=model,
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": system_tutor},
            {"role": "user", "content": f"{context}:\nQuestion{question}"}
        ]
    )
    content = response.choices[0].message.content
    if content is None:
        raise ValueError("Model returned no content in message.content")
    return json.loads(content)
