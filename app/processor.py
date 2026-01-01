import spacy
from typing import List, Dict

#Load the spacy model
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    print("Downloading spacy model...")
    spacy.cli.download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

def process_text(text: str) -> Dict:
    """
    Applies NLP preprocessing to user input:
    - Tokenization: Splitting text into words.
    - Lemmatization: Converting words to their root form.
    - Stopword removal: Removing common filler words (the, is, at).
    """
    doc = nlp(text.strip())

    lemmas = [
        token.lemma_.lower()
        for token in doc
        if not token.is_stop and not token.is_punct
        and not token.is_space
    ]

    return {
        "original_text": text,
        "lemmas": lemmas,
        "token_count": len(doc),
    }