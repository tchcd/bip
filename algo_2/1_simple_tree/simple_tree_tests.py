from simple_tree import SimpleTreeNode, SimpleTree
import pytest

def test_add_child():
    root = SimpleTreeNode(0, None)
    n1 = SimpleTreeNode(1, None)

    tree = SimpleTree(root)

    tree.AddChild(root, n1)

    assert n1.Parent == root
    assert n1 in root.Children
    assert tree.Root == root


def test_delete_node():
    root = SimpleTreeNode(val=0, parent=None)
    n1 = SimpleTreeNode(val=1, parent=None)
    n2 = SimpleTreeNode(val=2, parent=None)
    n3 = SimpleTreeNode(val=3, parent=None)
    tree = SimpleTree(root)
    tree.AddChild(root, n1)
    tree.AddChild(root, n2)
    tree.AddChild(n1, n3)
    tree.DeleteNode(n1)

    print(root)

    assert n1 not in root.Children


def test_get_all_nodes():
    root = SimpleTreeNode(val=0, parent=None)
    n1 = SimpleTreeNode(val=1, parent=None)
    n2 = SimpleTreeNode(val=2, parent=None)
    n3 = SimpleTreeNode(val=3, parent=None)
    n4 = SimpleTreeNode(val=4, parent=None)
    n5 = SimpleTreeNode(val=5, parent=None)
    tree = SimpleTree(root)
    tree.AddChild(root, n1)
    tree.AddChild(root, n2)
    tree.AddChild(n1, n3)
    tree.AddChild(n1, n4)
    tree.AddChild(n2, n5)

    tree.show_tree_level_with_values(root)

    nodes = tree.GetAllNodes()

    assert nodes == [root, n1,n3, n4, n2,  n5]


def test_find_nodes_by_value():
    root = SimpleTreeNode(val=1, parent=None)
    n1 = SimpleTreeNode(val=1, parent=None)
    n11 = SimpleTreeNode(val=1, parent=None)
    n3 = SimpleTreeNode(val=3, parent=None)
    n4 = SimpleTreeNode(val=4, parent=None)
    n5 = SimpleTreeNode(val=5, parent=None)
    tree = SimpleTree(root)
    tree.AddChild(root, n1)
    tree.AddChild(root, n11)
    tree.AddChild(n1, n3)
    tree.AddChild(n1, n4)
    tree.AddChild(n11, n5)

    print(root)

    nodes = tree.FindNodesByValue(1)

    assert nodes == [root, n1, n11]


def test_get_node_num():
    root = SimpleTreeNode(val=0, parent=None)
    n1 = SimpleTreeNode(val=1, parent=None)
    n2 = SimpleTreeNode(val=2, parent=None)
    n3 = SimpleTreeNode(val=3, parent=None)
    n4 = SimpleTreeNode(val=4, parent=None)
    n5 = SimpleTreeNode(val=5, parent=None)
    tree = SimpleTree(root)
    tree.AddChild(root, n1)
    tree.AddChild(root, n2)
    tree.AddChild(n1, n3)
    tree.AddChild(n1, n4)
    tree.AddChild(n2, n5)

    tree.show_tree_level_with_values()

    cnt = tree.Count()

    assert cnt == 6


def test_get_leafs_num():
    root = SimpleTreeNode(val=0, parent=None)
    n1 = SimpleTreeNode(val=1, parent=None)
    n2 = SimpleTreeNode(val=2, parent=None)
    n3 = SimpleTreeNode(val=3, parent=None)
    n4 = SimpleTreeNode(val=4, parent=None)
    n5 = SimpleTreeNode(val=5, parent=None)
    tree = SimpleTree(root)
    tree.AddChild(root, n1)
    tree.AddChild(root, n2)
    tree.AddChild(n1, n3)
    tree.AddChild(n1, n4)
    tree.AddChild(n2, n5)

    tree.show_tree_level_with_values()

    leafs = tree.LeafCount()

    assert leafs == 3


def test_count_two_1():
    root = SimpleTreeNode(val=0, parent=None)
    n1 = SimpleTreeNode(val=1, parent=None)


    tree = SimpleTree(root)
    tree.AddChild(root, n1)


    assert tree.Count() == 2
    assert tree.LeafCount() == 1


def test_leafs():
    root = SimpleTreeNode(val=0, parent=None)
    n1 = SimpleTreeNode(val=1, parent=None)
    n2 = SimpleTreeNode(val=2, parent=None)
    n3 = SimpleTreeNode(val=3, parent=None)
    n4 = SimpleTreeNode(val=4, parent=None)
    n5 = SimpleTreeNode(val=5, parent=None)


    tree = SimpleTree(root)
    tree.AddChild(root, n1)
    tree.AddChild(root, n2)
    tree.AddChild(n1, n3)
    tree.AddChild(n2, n4)
    tree.AddChild(n2, n5)

    tree.show_tree_level_with_values()

    assert tree.Count() == 6
    assert tree.LeafCount() == 3


def test_one_leaf():
    root = SimpleTreeNode(val=0, parent=None)

    tree = SimpleTree(root)

    tree.show_tree_level_with_values()

    assert tree.Count() == 1
    assert tree.LeafCount() == 1


if __name__ == '__main__':
    test_leafs()