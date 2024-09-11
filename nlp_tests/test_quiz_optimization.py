import spacy

class Question:
    def __init__(self, difficulty, topic, text):
        self.difficulty = difficulty
        self.topic = topic
        self.text = text

def create_quiz(num_questions, difficulty_level, topics):
    quiz = []
    for i in range(num_questions):
        question_text = f'Dummy question {i + 1} text.'
        quiz.append(Question(difficulty_level, topics[i % len(topics)], question_text))
    return quiz

def analyze_question(question):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(question.text)
    return len(doc.ents) > 0  

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

def test_create_quiz_with_nlp_analysis():
    """Test creating a quiz and analyze each question using spaCy"""
    num_questions = 3
    difficulty_level = "easy"
    topics = ["art", "music"]
    quiz = create_quiz(num_questions, difficulty_level, topics)

    for question in quiz:
        assert isinstance(question, Question)
        result = analyze_question(question)
        assert result  
