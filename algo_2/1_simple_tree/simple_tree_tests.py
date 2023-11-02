from simple_tree import SimpleTreeNode, SimpleTree


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

    print(root)

    nodes = tree.GetAllNodes()

    assert nodes == [root, n1, n2]


def test_find_nodes_by_value():
    root = SimpleTreeNode(val=0, parent=None)
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

    nodes = tree.GetAllNodes()

    assert nodes == [root, n1, n11]



if __name__ == '__main__':
    test_find_nodes_by_value()