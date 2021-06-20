from data_structure.data_structure.hashtable.hashtable import *
import pytest
from unittest.mock import patch

@patch('builtins.print')
def test_Adding_a_keyvalue_to_your_hashtable(mock_print):
    hashtable = Hashtable()
    hashtable.add('new','me')
    print(hashtable.get('new'))
    mock_print.assert_called_once_with('me')

def test_get_existed_key():
    expected = 'python'
    hashtable = Hashtable()
    hashtable.add('bad','python')
    actual = hashtable.get('bad')
    assert actual == expected

def test_returns_null_not_existed_key():
    expected = None
    hashtable = Hashtable()
    hashtable.add('B','yes')
    actual = hashtable.get('C')
    assert actual == expected



def test_conatin_key_true():
    hashtable = Hashtable()
    hashtable.add('JS','python')
    actual = hashtable.contains('JS')
    assert actual

def test_not_conatin_key():
    hashtable = Hashtable()
    hashtable.add('M','F')
    actual = hashtable.contains('not here')
    assert not actual

def test_hash_key_in_range():
    expected  = 1024
    hashtable = Hashtable()
    actual = hashtable.hash('Yes')
    assert actual in range(expected)