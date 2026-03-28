"""
tests_1c.py

This module contains unit tests for the max_subarray_sum function defined in lab_1c.py.
"""


import pytest 
from labs.lab_1.lab_1c import max_subarray_sum

def test_empty_list():
    assert max_subarray_sum(nums = []) == 0          # Test for an empty list
    
def test_different_lists():
    assert max_subarray_sum(nums = [0, 3, 4, 6,]) == 13         # Test for different lists
    assert max_subarray_sum(nums = [-1, -2, -3, -4,]) == -1         # Test for different lists
    assert max_subarray_sum(nums = [-2, 2, 6, 10,]) == 18         # Test for different lists
    assert max_subarray_sum(nums = [2, 4, -5, -4,]) == 6         # Test for different lists
   