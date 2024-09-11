import spacy

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

class Question:
    def __init__(self, text):
        self.text = text

class QuizCustomizer:
    def __init__(self, questions):
        self.questions = questions
        self.time_limit_enabled = False
        self.time_limit_duration = 0

    def enable_time_limit(self, duration, unit="minutes"):
        self.time_limit_enabled = True
        self.time_limit_duration = duration

    def disable_time_limit(self):
        self.time_limit_enabled = False
        self.time_limit_duration = 0

    def generate_quiz(self):
        if self.time_limit_enabled:
            # Logic to generate quiz with time limit
            pass
        else:
            # Logic to generate quiz without time limit
            pass

def test_enable_time_limit_option():
    """Test enabling the time limit option in the quiz customization interface."""
    quiz_customizer = QuizCustomizer([])
    quiz_customizer.enable_time_limit(duration=10)
    assert quiz_customizer.time_limit_enabled
    assert quiz_customizer.time_limit_duration == 10

def test_disable_time_limit_option():
    """Test disabling the time limit option in the quiz customization interface."""
    quiz_customizer = QuizCustomizer([])
    quiz_customizer.enable_time_limit(duration=10)
    quiz_customizer.disable_time_limit()
    assert not quiz_customizer.time_limit_enabled
    assert quiz_customizer.time_limit_duration == 0

def test_specify_time_limit_duration():
    """Test specifying the time limit duration for quiz completion."""
    quiz_customizer = QuizCustomizer([])
    quiz_customizer.enable_time_limit(duration=5, unit="seconds")
    assert quiz_customizer.time_limit_enabled
    assert quiz_customizer.time_limit_duration == 5

def test_quiz_adherence_to_time_limit():
    """Test that the generated quiz adheres to the specified time limit."""
    questions = [Question("Question 1"), Question("Question 2"), Question("Question 3")]
    quiz_customizer = QuizCustomizer(questions)
    
    # Enable time limit for 1 minute
    quiz_customizer.enable_time_limit(duration=1, unit="minutes")
    
    # Mock logic to generate quiz within time limit
    generated_quiz = quiz_customizer.generate_quiz()
    
    # Mock logic to simulate quiz taking within the time limit
    quiz_in_progress = True
    time_elapsed = 0
    
    while quiz_in_progress:
        # Mock logic to simulate quiz taking, incrementing time elapsed
        time_elapsed += 1
        
        # If time limit is reached, end the quiz
        if time_elapsed >= 1 * 60:  # 1 minute in seconds
            quiz_in_progress = False
    
    assert not quiz_customizer.time_limit_enabled

def test_countdown_timer_display():
    """Test that participants see a visible countdown timer during the quiz."""
    quiz_customizer = QuizCustomizer([])
    quiz_customizer.enable_time_limit(duration=2, unit="minutes")
    
    # Mock logic to generate quiz with time limit
    generated_quiz = quiz_customizer.generate_quiz()
    
    # Mock logic to simulate quiz taking with countdown timer display
    time_elapsed = 0
    
    while time_elapsed < 2 * 60:  # 2 minutes in seconds
        # Mock logic to simulate quiz taking, incrementing time elapsed
        time_elapsed += 1
        
        # Mock logic to check if the countdown timer is displayed to participants
        assert countdown_timer_is_displayed_to_participants()
