from data_structure.data_structure.quick_sort.quick_sort import quick_sort
import pytest

def test_sort_empty():
    actual = quick_sort([])
    expected = []
    assert actual == expected

def test_one_sort():
    actual = quick_sort([2])
    expected = [2]
    assert actual == expected

def test_two_sort():
    actual = quick_sort([8,4,23,42,16,15])
    expected = [4, 8, 15, 16, 23, 42]
    assert actual == expected

def test_three_sort():
    actual = quick_sort([1,5,2,-7,72])
    expected = [-7, 1, 2, 5, 72]
    assert actual == expected
