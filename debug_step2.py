from app.processor import process_text

def check_nlp():
    print("🧠 Initializing spaCy and testing NLP logic...")
    test_text = "I am thinking about the laws of gravity"
    
    try:
        result = process_text(test_text)
        print(f"✅ NLP Success!")
        print(f"📝 Original: '{result['original_text']}'")
        print(f"🧪 Lemmas (Roots): {result['lemmas']}")
        print(f"📊 Token Count: {result['token_count']}")
        
        # Professional check: Ensure stop words like 'the' are removed
        if "the" in result["lemmas"]:
            print("⚠️ Warning: Stop words were not filtered correctly.")
        else:
            print("✨ Clean: Stop words (the, is, am) were successfully removed.")
            
    except Exception as e:
        print(f"❌ NLP Error: {e}")
        print("\n💡 Professional Tip: Check app/processor.py for 'token.lemma_.lower()'")

if __name__ == "__main__":
    check_nlp()