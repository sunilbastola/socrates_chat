from huggingface_hub import InferenceClient
from app.config import settings

client = InferenceClient(api_key=settings.HF_TOKEN)

def generate_response(user_input: str):
    """Generate a response from the Socrates model."""

    system_prompt = """
    You are socrates, the wise teacher for the modern day learners,
    For any responses, you do not provide direct answers, insted you teach the
    user to think from the first principles and build their own understanding.
    """

    completion = client.chat.completions.create(
        model=settings.MODEL_ID,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input},
        ],
    )
    return completion.choices[0].message.content


if __name__ == "__main__":
    print()