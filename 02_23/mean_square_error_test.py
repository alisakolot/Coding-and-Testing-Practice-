# import unittest
# import mean_square_error_test

# class MeanSquareErrorTest(unittest.TestCase):
#     def test1(self):
        
#         a1 = [1,2,3]
#         a2 = [4,5,6]
#         self.assertEqual(solution(a1, a2), 9)

#     def test2(self):
#         b1 = [10, 20, 10, 2]
#         b2 = [10, 25, 5, -2]
#         self.assertEqual(solution(b1, b2), 16.5)


import pytest
from mean_square_error_test import solution


a1 = [1,2,3]
a2 = [4,5,6]
def test1():
    assert solution(a1, a2) == 9

b1 = [10, 20, 10, 2]
b2 = [10, 25, 5, -2]
def test2(b1, b2):
    assert solution(b1, b2) == 16.5