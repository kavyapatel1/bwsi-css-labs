"""
tests_1d.py

This module contains unit tests for the two_sum function defined in lab_1d.py.
"""


import pytest 
from labs.lab_1.lab_1d import two_sum

def test_empty_list():
    assert two_sum(nums = [], target = 4) == []          # Test for an empty list
    
def test_different_lists():
    assert two_sum(nums = [0, 3, 4, 6,], target = 2) == []        # Test for different lists
    assert two_sum(nums = [-1, -6, -3, -4,], target = -5) == [0, 3]       # Test for different lists
    assert two_sum(nums = [0, 2, 6, 10,], target = 6) == [0, 2]         # Test for different lists
    assert two_sum(nums = [2, 4, -5, -4,], target = -1 ) == [1, 2]         # Test for different lists
    assert two_sum(nums = [5, 4, 5, 12,], target = 10 ) == [0, 2]         # Test for different lists
