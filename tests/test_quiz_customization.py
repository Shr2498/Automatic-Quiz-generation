import pytest

class Question:
    def __init__(self, difficulty, topic, text):
        self.difficulty = difficulty
        self.topic = topic
        self.text = text
        
def create_quiz(num_questions, difficulty_level, topics):
    pass

def test_create_quiz_with_specific_number_of_questions():
    """Test creating a quiz with a specific number of questions"""
    num_questions = 10
    difficulty_level = "easy"
    topics = ["geography", "science"]
    quiz = create_quiz(num_questions, difficulty_level, topics)
    
    assert len(quiz) == num_questions

def test_create_quiz_with_difficulty_level():
    """Test creating a quiz with a specific difficulty level"""
    num_questions = 5
    difficulty_level = "medium"
    topics = ["history", "math"]
    quiz = create_quiz(num_questions, difficulty_level, topics)

    for question in quiz:
        assert isinstance(question, Question)
        assert question.difficulty == difficulty_level

def test_create_quiz_with_invalid_difficulty_level():
    """Test creating a quiz with an invalid difficulty level"""
    num_questions = 3
    difficulty_level = "invalid_level"
    topics = ["art", "music"]
    
    with pytest.raises(ValueError):
        create_quiz(num_questions, difficulty_level, topics)

def test_create_quiz_with_no_topics():
    """Test creating a quiz with no specified topics"""
    num_questions = 6
    difficulty_level = "easy"
    topics = []
    
    with pytest.raises(ValueError):
        create_quiz(num_questions, difficulty_level, topics)