
import os
from dotenv import load_dotenv
from groq import Groq, APIError

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def generate_answer(question: str) -> str:
    try:
        response = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[
                {
                    "role": "user",
                    "content": question
                }
            ]
        )

        answer = response.choices[0].message.content
        return answer

    except APIError as error:
        print(f"Groq API error: {error}")
        raise
