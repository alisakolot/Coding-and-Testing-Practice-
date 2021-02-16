import pytest

# def func(x):
#     return x +  5

# def test_method():
#     assert func(3) == 8

# Running Files
@pytest.mark.one
def test_method1():
    x = 5 
    y = 10
    assert x == y 
@pytest.mark.one
def test_method2():
    a = 15
    b = 20
    assert a + 5 == b

    
