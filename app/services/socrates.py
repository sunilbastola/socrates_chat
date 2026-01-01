import os
from huggingface_hub import InferenceClient
from app.config import settings

# Initialize client safely using the pre-verified settings object
client = InferenceClient(api_key=settings.HF_TOKEN)

def generate_response(user_input: str):
    """Generate a response using Hugging Face Inference API with explicit error handling."""
    
    system_prompt = (
        "You are Socrates, the wise teacher for modern-day learners. "
        "Do not provide direct answers. Instead, teach the user to think "
        "from first principles. End every response with a probing question."
    )

    # List of models to try in order of preference
    # Using a list makes the code more maintainable/readable (DRY principle)
    models_to_try = [
        settings.MODEL_ID,                   # Primary: Llama-3.1-8B
        "mistralai/Mistral-7B-Instruct-v0.3", # Fallback 1
        "HuggingFaceH4/zephyr-7b-beta"        # Fallback 2
    ]

    for model in models_to_try:
        try:
            completion = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_input},
                ],
                max_tokens=200,
                temperature=0.7
            )
            return completion.choices[0].message.content

        except Exception as e:
            error_msg = str(e)
            
            # --- Specific Error Handling for API Limits ---
            if "429" in error_msg:
                print(f"🚀 Rate Limit (429) hit on {model}. Trying next model...")
                continue # Move to the next model in the list
            
            elif "503" in error_msg:
                print(f"⏳ Model Overload (503) on {model}. Trying next model...")
                continue # Move to the next model in the list
            
            # If it's not a limit issue, log it and try the next model anyway
            print(f"⚠️ Error with {model}: {error_msg[:50]}")
            continue

    # Final fallback if all models in the list fail
    return (
        "My apologies, traveler. The marketplace of ideas is quite crowded today, "
        "and my thoughts are momentary clouded. Shall we try again in a moment?"
    )