import spacy

nlp = spacy.load("en_core_web_sm")

def validate_test_subject(test):
    """
    Check if the test has a valid subject type using spaCy for NLP analysis.
    """
    doc = nlp(test.get("question", ""))
    nouns = [token.text.lower() for token in doc if token.pos_ == "NOUN"]

    return len(nouns) > 0

def test_more_than_one_subject_type():
    """Check that there is at least more than 1 subject type"""
    total_tests = [
        {"subject": "geography", "question": "What is the capital of France?"},
        {"subject": "math", "question": "What is 2 + 2?"},
    ]

    valid_tests = [test for test in total_tests if validate_test_subject(test)]
    assert len(set(test["subject"] for test in valid_tests)) > 1
