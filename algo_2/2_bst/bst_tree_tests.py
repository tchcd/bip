from bst import BST, BSTNode
import pytest


def test_bfs_normal():
    root = BSTNode(8, 8, None)
    bst = BST(root)

    bst.AddKeyValue(4, 4)
    bst.AddKeyValue(12, 12)
    bst.AddKeyValue(2, 2)
    bst.AddKeyValue(6, 6)
    bst.AddKeyValue(10, 10)
    bst.AddKeyValue(9, 9)
    bst.AddKeyValue(11, 11)
    bst.AddKeyValue(14, 14)
    bst.AddKeyValue(13, 13)

    assert [n.NodeKey for n in bst.WideAllNodes()] == [8, 4, 12, 2, 6, 10, 14, 9, 11, 13]


def test_bfs_root():
    root = BSTNode(8, 8, None)
    bst = BST(root)

    assert bst.WideAllNodes() == [root]


def test_bfs_none():
    bst = BST(None)
    assert bst.WideAllNodes() == []


def test_dfs_in_order_normal():
    root = BSTNode(8, 8, None)
    bst = BST(root)

    bst.AddKeyValue(4, 4)
    bst.AddKeyValue(12, 12)
    bst.AddKeyValue(2, 2)
    bst.AddKeyValue(6, 6)
    bst.AddKeyValue(10, 10)
    bst.AddKeyValue(9, 9)
    bst.AddKeyValue(11, 11)
    bst.AddKeyValue(14, 14)
    bst.AddKeyValue(13, 13)

    assert [n.NodeKey for n in bst.DeepAllNodes(0)] == [2, 4, 6, 8, 9, 10, 11, 12, 13, 14]


def test_dfs_in_order_none():
    bst = BST(None)

    assert [n.NodeKey for n in bst.DeepAllNodes(0)] == []


def test_dfs_in_order_one():
    root = BSTNode(8, 8, None)
    bst = BST(root)

    assert [n.NodeKey for n in bst.DeepAllNodes(0)] == [8]


def test_dfs_in_order_three():
    root = BSTNode(8, 8, None)
    bst = BST(root)

    bst.AddKeyValue(4, 4)
    bst.AddKeyValue(12, 12)

    assert [n.NodeKey for n in bst.DeepAllNodes(0)] == [4, 8, 12]


def test_dfs_post_order_normal():
    root = BSTNode(8, 8, None)
    bst = BST(root)

    bst.AddKeyValue(4, 4)
    bst.AddKeyValue(12, 12)
    bst.AddKeyValue(2, 2)
    bst.AddKeyValue(6, 6)
    bst.AddKeyValue(10, 10)
    bst.AddKeyValue(9, 9)
    bst.AddKeyValue(11, 11)
    bst.AddKeyValue(14, 14)
    bst.AddKeyValue(13, 13)

    assert [n.NodeKey for n in bst.DeepAllNodes(1)] == [2, 6, 4, 9, 11, 10, 13, 14, 12, 8]


def test_dfs_pre_order_normal():
    root = BSTNode(8, 8, None)
    bst = BST(root)

    bst.AddKeyValue(4, 4)
    bst.AddKeyValue(12, 12)
    bst.AddKeyValue(2, 2)
    bst.AddKeyValue(6, 6)
    bst.AddKeyValue(10, 10)
    bst.AddKeyValue(9, 9)
    bst.AddKeyValue(11, 11)
    bst.AddKeyValue(14, 14)
    bst.AddKeyValue(13, 13)

    assert [n.NodeKey for n in bst.DeepAllNodes(2)] == [8, 4, 2, 6, 12, 10, 9, 11, 14, 13]
