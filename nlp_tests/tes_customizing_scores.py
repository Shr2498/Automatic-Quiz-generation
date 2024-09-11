import spacy

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

class Question:
    def __init__(self, text, correct_answer):
        self.text = text
        self.correct_answer = correct_answer

class QuizCustomizer:
    def __init__(self, questions):
        self.questions = questions
        self.scoring_enabled = False
        self.points_per_question = 1

    def enable_scoring(self, points_per_question=1):
        self.scoring_enabled = True
        self.points_per_question = points_per_question

    def disable_scoring(self):
        self.scoring_enabled = False
        self.points_per_question = 1

    def calculate_score(self, participant_answers):
        score = 0
        for idx, participant_answer in enumerate(participant_answers):
            # Check if the answer is correct
            correct_answer = self.questions[idx].correct_answer
            if participant_answer == correct_answer:
                score += self.points_per_question
        return score

def test_enable_scoring_configuration():
    """Test enabling scoring configuration in the quiz customization interface."""
    quiz_customizer = QuizCustomizer([])
    quiz_customizer.enable_scoring()
    assert quiz_customizer.scoring_enabled
    assert quiz_customizer.points_per_question == 1

def test_disable_scoring_configuration():
    """Test disabling scoring configuration in the quiz customization interface."""
    quiz_customizer = QuizCustomizer([])
    quiz_customizer.enable_scoring()
    quiz_customizer.disable_scoring()
    assert not quiz_customizer.scoring_enabled
    assert quiz_customizer.points_per_question == 1

def test_specify_points_per_question():
    """Test specifying points per question in the quiz customization interface."""
    quiz_customizer = QuizCustomizer([])
    quiz_customizer.enable_scoring(points_per_question=2)
    assert quiz_customizer.scoring_enabled
    assert quiz_customizer.points_per_question == 2

def test_zero_points_for_unanswered_questions():
    """Test that participants receive zero points for unanswered questions."""
    questions = [Question("Question 1", "A"), Question("Question 2", "B"), Question("Question 3", "C")]
    quiz_customizer = QuizCustomizer(questions)
    
    # Enable scoring with 1 point per question
    quiz_customizer.enable_scoring(points_per_question=1)
    
    # Mock logic to simulate a participant's answers
    participant_answers = ["A", "B"]  # Leaving the third question unanswered
    
    # Calculate the score
    score = quiz_customizer.calculate_score(participant_answers)
    
    # Ensure that the score is calculated correctly, considering zero points for unanswered questions
    assert score == 2

def test_cumulative_scoring():
    """Test that the scoring system accurately calculates cumulative scores."""
    questions = [Question("Question 1", "A"), Question("Question 2", "B"), Question("Question 3", "C")]
    quiz_customizer = QuizCustomizer(questions)
    
    # Enable scoring with 2 points per question
    quiz_customizer.enable_scoring(points_per_question=2)
    
    # Mock logic to simulate a participant's answers
    participant_answers = ["A", "B", "C"]  # All answers are correct
    
    # Calculate the score
    score = quiz_customizer.calculate_score(participant_answers)
    
    # Ensure that the cumulative score is calculated correctly
    assert score == 6
