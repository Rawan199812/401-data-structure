import pytest
from data_structure.data_structure.insertion_sort.insertion_sort import insertion_sort

def test_insertion_sort_integers_values_one():
    expected = [4, 8, 15, 16, 23, 42]
    actual = insertion_sort([8,4,23,42,16,15])
    assert actual == expected