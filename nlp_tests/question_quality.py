import pytest
import spacy

# Load the spaCy English model
nlp = spacy.load("en_core_web_sm")

def analyze_question_clarity(question):
    """
    Analyze the clarity of a generated question using spaCy.
    """
    doc = nlp(question)
    
    # Example: Check if the question has a clear subject
    has_clear_subject = any(token.dep_ in ["nsubj", "nsubjpass"] for token in doc)
    
    return has_clear_subject

def analyze_question_relevance(question, context):
    """
    Analyze the relevance of a generated question to a given context.
    """
    doc_question = nlp(question)
    doc_context = nlp(context)
    
    # Example: Check if key terms from the question are present in the context
    key_terms_present = any(token.text in doc_context.text for token in doc_question if token.is_alpha)
    
    return key_terms_present

def generate_quality_test_case(question, expected_quality):
    """
    Generate a test case for assessing the quality of a generated question.
    """
    return pytest.param(
        question,
        expected_quality,
        id=f"quality_test_{expected_quality}",
    )


# Corrected expected_quality values
quality_test_cases = [
    generate_quality_test_case("What is the capital of France?", "high_clarity_relevant"),
    generate_quality_test_case("Which programming language is known for its simplicity?", "high_clarity_relevant"),
    generate_quality_test_case("Who is the author of 'To Kill a Mockingbird'?", "low_clarity_relevant"),
    generate_quality_test_case("What is the largest planet in our solar system?", "high_clarity_irrelevant"),
    generate_quality_test_case("Which color is not in the rainbow?", "high_clarity_irrelevant"),
]


def get_relevant_context_for_question(question):
    """
    Provide a relevant context for the given question.
    """
    question_lower = question.lower()
    if "capital of france" in question_lower:
        return "Paris is the capital of France."
    elif "programming language is known for its simplicity" in question_lower:
        return "Python is known for its simplicity."
    elif "author of 'to kill a mockingbird'" in question_lower:
        return "Harper Lee is the author of 'To Kill a Mockingbird.'"
    elif "largest planet in our solar system" in question_lower:
        return "Jupiter is the largest planet in our solar system."
    elif "color is not in the rainbow" in question_lower:
        return "Black is not in the rainbow."

    # If the question doesn't match known patterns, return a generic context
    return "This is a generic context for the question."

# Use pytest.mark.parametrize to create parameterized tests
@pytest.mark.parametrize("question, expected_quality", quality_test_cases)
def test_question_quality(question, expected_quality):
    # Analyze question clarity
    has_clear_subject = analyze_question_clarity(question)

    # Analyze question relevance using a relevant context
    context = get_relevant_context_for_question(question)
    key_terms_present = analyze_question_relevance(question, context)

    # Assess overall question quality based on clarity and relevance
    is_high_quality = has_clear_subject and key_terms_present

    assert is_high_quality if expected_quality == "high_clarity_relevant" else not is_high_quality
