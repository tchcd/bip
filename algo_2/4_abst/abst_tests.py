from abst import aBST


def test_abst_add():
    tree = aBST(1)
    tree.AddKey(8)
    tree.AddKey(12)
    tree.AddKey(4)
    assert tree.Tree == [8, 4, 12]


def test_abst_add2():
    tree = aBST(2)
    tree.AddKey(8)
    tree.AddKey(12)
    tree.AddKey(4)
    tree.AddKey(6)
    tree.AddKey(2)
    tree.AddKey(10)
    assert tree.Tree == [8, 4, 12, 2, 6, 10, None]


def test_abst_empty():
    tree = aBST(0)
    assert tree.Tree == [None]


def test_abst_one():
    tree = aBST(0)
    tree.AddKey(8)
    tree.AddKey(2)
    assert tree.Tree == [8]

