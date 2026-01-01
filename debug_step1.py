from app.config import settings
from huggingface_hub import HfApi

def check_env():
    print(f"🔍 BASE_DIR: {settings.BASE_DIR}")
    print(f"🔑 Token starts with: {str(settings.HF_TOKEN)[:8]}...")
    
    api = HfApi()
    try:
        user_info = api.whoami(token=settings.HF_TOKEN)
        print(f"✅ HF Auth Success! Logged in as: {user_info['name']}")
    except Exception as e:
        print(f"❌ HF Auth Failed: {e}")

if __name__ == "__main__":
    check_env()