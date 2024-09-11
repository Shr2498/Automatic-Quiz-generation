# Tests for Issue 8

# Import-related tests
def test_import_button_exists():
    """
    Check to see if the button exists   
    """
    with open("login.html", 'r') as f:
        assert "<button" in f.read()

def test_import_function_type():
    """
    Ensure import functionality works    
    """
    csv_content = "question1,answer1\nquestion2,answer2"
    assert isinstance(import_questions(csv_content), list)

def test_import_function_correctness():
    """
    Ensure the import functionality works correctly
    """
    csv_content = "question1,answer1\nquestion2,answer2"
    result = import_questions(csv_content)
    assert len(result) == 2
    assert isinstance(result[0], Question)
    assert isinstance(result[1], Question)

def test_quiz_export():
    """
    Check the export type of the questions and answers    
    """
    export = quiz_export()
    for question, response in export:
        assert isinstance(question, Question)
        assert isinstance(response, Response)

def test_import():
    """
    Test the import functionality on all the dummy CSVs    
    """
    # TODO: Add test cases for different CSV files

def test_export():
    """
    Test the export functionality on all the dummy CSVs    
    """
    # TODO: Add test cases for different scenarios
