import pytest
from sum_odd_even import * 

def test_basic_tests():
    assert odd_or_even([0, 1, 1]) == "even"
    assert odd_or_even([13, 7, 80]) == "even"
    assert odd_or_even([40, 2, 55]) == "odd"
    assert odd_or_even([8, 5, 2]) == "odd"

