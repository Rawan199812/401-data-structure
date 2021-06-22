from data_structure.challenges.left_join.left_join import *
def test_None():
    hash_1 = Hashtable()
    hash_1.add('1','A')
    hash_1.add('2','B')
    hash_1.add('3','C')
    hash_1.add('4','D')

    hash_2 = Hashtable()
    actual = left_join_hash(hash_1,hash_2)
    expected = [['1','A',None],['2','B',None],['3','C',None],['4','D',None],]
    assert actual == expected

def test_empty_hashs():
    hash_1 = Hashtable()
    hash_2 = Hashtable()
    actual = left_join_hash(hash_1,hash_2)
    expected = []
    assert actual == expected