import pytest
import spacy
from your_quiz_module import import_questions, export_questions, quiz_export

# Load the spaCy English model
nlp = spacy.load("en_core_web_sm")

# Mocked data for testing purposes
sample_quiz_data = [
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "2 + 2 equals?", "answer": "4"},
]

def analyze_text_for_entities(text):
    """
    Analyze text using spaCy and return named entities.
    """
    doc = nlp(text)
    return [ent.text for ent in doc.ents]

def generate_import_test_case(external_source):
    """
    Generate a test case for importing questions from an external source.
    """
    # Mock an external source with named entities
    external_source_entities = analyze_text_for_entities(external_source)

    # Generate the test case
    return pytest.param(
        external_source,
        external_source_entities,
        id=f"import_from_{external_source_entities}",
    )

def generate_export_test_case(questions):
    """
    Generate a test case for exporting questions.
    """
    # Mock questions with named entities
    questions_entities = []
    for q in questions:
        question_entities = analyze_text_for_entities(q["question"])
        answer_entities = analyze_text_for_entities(q["answer"])
        questions_entities.extend(question_entities + answer_entities)

    # Generate the test case
    return pytest.param(
        questions,
        questions_entities,
        id=f"export_with_{questions_entities}",
    )

# Generate import test cases
import_test_cases = [
    generate_import_test_case("questions from a history quiz"),
    generate_import_test_case("questions related to science"),
    # Add more import test cases as needed
]

# Generate export test cases
export_test_cases = [
    generate_export_test_case(sample_quiz_data),
    generate_export_test_case([
        {"question": "Who is the president of the USA?", "answer": "Joe Biden"},
        {"question": "What is the largest mammal?", "answer": "Blue Whale"},
        # Add more questions as needed
    ]),
    # Add more export test cases as needed
]

# Use pytest.mark.parametrize to create parameterized tests
@pytest.mark.parametrize("external_source, expected_entities", import_test_cases)
def test_import_questions_with_entities(external_source, expected_entities):
    imported_questions = import_questions(external_source)
    assert isinstance(imported_questions, list)

    # Extract entities from the imported questions for assertion
    imported_entities = []
    for q in imported_questions:
        question_entities = analyze_text_for_entities(q["question"])
        answer_entities = analyze_text_for_entities(q["answer"])
        imported_entities.extend(question_entities + answer_entities)

    assert set(expected_entities) <= set(imported_entities)

@pytest.mark.parametrize("questions, expected_entities", export_test_cases)
def test_export_questions_with_entities(questions, expected_entities):
    # Export questions
    exported_data = quiz_export(questions)

    # Extract entities from the exported data for assertion
    exported_entities = []
    for question, response in exported_data:
        question_entities = analyze_text_for_entities(question)
        response_entities = analyze_text_for_entities(response)
        exported_entities.extend(question_entities + response_entities)

    assert set(expected_entities) <= set(exported_entities)
