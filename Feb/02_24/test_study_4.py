from num_carries import * 

def test_num_of_carries():
    assert number_of_carries(543, 3456) == 0
    assert number_of_carries(1927,6426) == 2

def test_outliers():
    assert number_of_carries(0, 0) == 0
    assert number_of_carries(16, -90) == 0

def test_b_length():
    b = 1
    assert number_of_carries(3, b) == 0
    assert number_of_carries(9999, b) == 4
