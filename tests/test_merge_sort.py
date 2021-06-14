import pytest
from data_structure.data_structure.merge_sort.merge_sort import merge_sort

def test_merge_sort_integers():
    expected = [4, 8, 15, 16, 23, 42]
    actual = merge_sort([8,4,23,42,16,15])
    assert actual == expected