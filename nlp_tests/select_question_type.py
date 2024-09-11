# File: select_question_type.py

import pytest

def select_question_type(question_type):
    supported_types = ["Multiple Choice", "Fill in the Blanks", "True/False"]
    
    if question_type is None or question_type == "":
        raise ValueError("Please select a question type")

    # Case-insensitive comparison
    question_type_lower = question_type.lower()
    if question_type_lower not in map(str.lower, supported_types):
        raise ValueError("Invalid question type. Please select from: {}".format(", ".join(supported_types)))

    return question_type

def test_select_multiple_choice():
    # Test case for selecting "Multiple Choice" question type
    selected_question_type = select_question_type("Multiple Choice")
    assert selected_question_type == "Multiple Choice"

def test_select_fill_in_the_blanks():
    # Test case for selecting "Fill in the Blanks" question type
    selected_question_type = select_question_type("Fill in the Blanks")
    assert selected_question_type == "Fill in the Blanks"

def test_select_true_false():
    # Test case for selecting "True/False" question type
    selected_question_type = select_question_type("True/False")
    assert selected_question_type == "True/False"

def test_select_invalid_question_type():
    # Test case for selecting an invalid question type
    with pytest.raises(ValueError, match="Invalid question type"):
        select_question_type("Invalid Question Type")
