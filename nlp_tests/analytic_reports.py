import pytest
import spacy
from your_analytics_module import generate_performance_report, analyze_trend, export_data

# Load the spaCy English model
nlp = spacy.load("en_core_web_sm")

# Mocked data for testing purposes
sample_performance_data = [
    {"user_id": 1, "score": 90, "time_taken": 30, "feedback": "Well done!"},
    {"user_id": 2, "score": 80, "time_taken": 40, "feedback": "Good effort."},
    {"user_id": 3, "score": 95, "time_taken": 25, "feedback": "Excellent work!"},
]

def analyze_feedback_sentiment(feedback):
    """
    Analyze the sentiment of feedback using spaCy.
    """
    doc = nlp(feedback)
    return doc.sentiment

def generate_feedback_sentiment_test_case(feedback, expected_sentiment):
    """
    Generate a test case for analyzing the sentiment of feedback.
    """
    return pytest.param(
        feedback,
        expected_sentiment,
        id=f"analyze_feedback_sentiment_{expected_sentiment}",
    )

# Generate sentiment analysis test cases for feedback
sentiment_test_cases = [
    generate_feedback_sentiment_test_case("Well done!", "positive"),
    generate_feedback_sentiment_test_case("Good effort.", "positive"),
    generate_feedback_sentiment_test_case("Excellent work!", "positive"),
    generate_feedback_sentiment_test_case("Needs improvement.", "negative"),
]

# Use pytest.mark.parametrize to create parameterized tests
@pytest.mark.parametrize("feedback, expected_sentiment", sentiment_test_cases)
def test_analyze_feedback_sentiment(feedback, expected_sentiment):
    sentiment = analyze_feedback_sentiment(feedback)
    assert sentiment == expected_sentiment
