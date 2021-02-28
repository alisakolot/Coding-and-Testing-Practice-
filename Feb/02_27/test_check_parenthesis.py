import pytest
from check_parenthesis import * 

def test_valid_parenthesis():
    assert valid_parentheses("  (") == False
    assert valid_parentheses(")test") ==  False
    assert valid_parentheses("") == True
    assert valid_parentheses("hi())(") == False
    assert valid_parentheses("hi(hi)()") == True