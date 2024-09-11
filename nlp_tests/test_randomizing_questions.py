import spacy

nlp = spacy.load("en_core_web_sm")

class Question:
    def __init__(self, difficulty, subject, text):
        self.difficulty = difficulty
        self.subject = subject
        self.text = text

# Sample list of questions
questions = [
    Question("easy", "geography", "What is the capital of France?"),
    Question("medium", "math", "What is 2 + 2?"),
    Question("easy", "science", "Name the four seasons."),
    Question("hard", "history", "Who was the first president of the United States?"),
    Question("medium", "literature", "Who wrote Romeo and Juliet?"),
]

def randomize_questions(questions, difficulty=None, subject=None):
    # Filter questions based on specified difficulty or subject
    filtered_questions = questions
    if difficulty:
        filtered_questions = [q for q in filtered_questions if q.difficulty == difficulty]
    if subject:
        filtered_questions = [q for q in filtered_questions if q.subject == subject]

    # Shuffle the filtered questions using spaCy
    random.shuffle(filtered_questions)

    # Combine shuffled questions with remaining questions
    randomized_questions = filtered_questions + [q for q in questions if q not in filtered_questions]

    return randomized_questions

def test_enable_randomization_option():
    """Test enabling the randomization option in the quiz customization interface."""
    quiz_customizer = QuizCustomizer()
    quiz_customizer.enable_randomization()
    assert quiz_customizer.is_randomization_enabled()

def test_disable_randomization_option():
    """Test disabling the randomization option in the quiz customization interface."""
    quiz_customizer = QuizCustomizer(randomization_enabled=True)
    quiz_customizer.disable_randomization()
    assert not quiz_customizer.is_randomization_enabled()

def test_shuffle_questions_within_difficulty():
    """Test shuffling questions within a specified difficulty level."""
    quiz_customizer = QuizCustomizer(questions)
    
    # Enable randomization and specify difficulty level
    quiz_customizer.enable_randomization(difficulty="easy")
    randomized_quiz = quiz_customizer.generate_quiz()

    # Ensure questions within the specified difficulty are shuffled
    shuffled_questions = [q.text for q in randomized_quiz]
    original_questions = [q.text for q in questions if q.difficulty == "easy"]
    assert set(shuffled_questions) == set(original_questions)

def test_shuffle_questions_within_subject():
    """Test shuffling questions within a specified subject."""
    quiz_customizer = QuizCustomizer(questions)

    # Enable randomization and specify subject
    quiz_customizer.enable_randomization(subject="geography")
    randomized_quiz = quiz_customizer.generate_quiz()

    # Ensure questions within the specified subject are shuffled
    shuffled_questions = [q.text for q in randomized_quiz]
    original_questions = [q.text for q in questions if q.subject == "geography"]
    assert set(shuffled_questions) == set(original_questions)

def test_shuffle_questions_within_difficulty_and_subject():
    """Test shuffling questions within a specified difficulty level and subject."""
    quiz_customizer = QuizCustomizer(questions)

    # Enable randomization and specify difficulty level and subject
    quiz_customizer.enable_randomization(difficulty="medium", subject="geography")
    randomized_quiz = quiz_customizer.generate_quiz()

    # Ensure questions within the specified difficulty and subject are shuffled
    shuffled_questions = [q.text for q in randomized_quiz]
    original_questions = [q.text for q in questions if q.difficulty == "medium" and q.subject == "geography"]
    assert set(shuffled_questions) == set(original_questions)

def test_no_randomization_by_default():
    """Test that questions are not randomized by default."""
    quiz_customizer = QuizCustomizer(questions)
    randomized_quiz = quiz_customizer.generate_quiz()

    # Ensure questions remain in their original order by default
    original_questions = [q.text for q in questions]
    assert [q.text for q in randomized_quiz] == original_questions
