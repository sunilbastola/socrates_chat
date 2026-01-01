from app.services.socrates import generate_response

def check_ai():
    print("🤖 Sending inquiry to the Philosopher (Llama 3.1)...")
    test_input = "I want to learn about gravity"
    
    try:
        response = generate_response(test_input)
        print(f"✅ AI Success!")
        print(f"🏛️  Socrates says: \"{response}\"")
        
        # Professional Check: Ensure he's actually asking a question
        if "?" in response:
            print("✨ Quality Check: Socrates asked a question. Good pedagogy!")
        else:
            print("⚠️  Warning: Response was not a question. Check your system prompt.")
            
    except Exception as e:
        print(f"❌ AI Error: {e}")
        print("\n💡 Tip: If you see a 404, we may need to use a different model or router in socrates.py.")

if __name__ == "__main__":
    check_ai()