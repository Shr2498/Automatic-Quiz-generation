def test_button_exists():
    """Checks to see if login button exists"""
    with open("login.html", 'r') as f:
        assert "login" in f.read().lower()


    
