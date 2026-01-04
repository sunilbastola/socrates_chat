import os
from huggingface_hub import InferenceClient
from app.config import settings

# Use the V1 Router - this is the exact endpoint your second curl hit
client = InferenceClient(
    api_key=settings.HF_TOKEN,
)

def generate_response(user_input: str):
    system_prompt = (
        "You are Socrates, the wise teacher. Do not provide direct answers. "
        "Instead, teach the user to think from first principles. "
        "End every response with a probing question."
    )

    model_id = "meta-llama/Llama-3.1-8B-Instruct"

    try:
        completion = client.chat.completions.create(
            model=model_id,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_input},
            ],
            max_tokens=250,
            temperature=0.7,
        )
        return (completion.choices[0].message)

    except Exception as e:
        print(f"API Error: {str(e)}")

        return (
            "My apologies, traveler. The marketplace of ideas is quite crowded today, "
            "and my thoughts are momentary clouded. Shall we try again in a moment?"
        )