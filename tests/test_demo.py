
from my_new_project import my_amazing_function, my_sick_function

def test_true() -> None:
    """Dummy test🌴🥥"""
    assert True

def test_my_amazing_function() -> None:
    """Test the my_amazing_function"""
    result = my_amazing_function()
    assert result == "Hello, World!"

def test_my_sick_function() -> None:
    """Test the my_sick_function"""
    result = my_sick_function("Hello, ", "World!")
    assert result == "Hello, World!"
