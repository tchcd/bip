from bst import BST, BSTNode
import pytest


if __name__ == '__main__':
    root = BSTNode(8, 'eight', None)
    bst = BST(root)
    n1 = BSTNode(4, 'four', None)
    n2 = BSTNode(12, 'twelve', None)
    n3 = BSTNode(2, 'two', None)
    n4 = BSTNode(6, 'six', None)

    root.LeftChild = n1
    root.RightChild = n2

    n1.Parent = root
    n2.Parent = root

    n1.LeftChild = n3
    n1.RightChild = n4
    n3.Parent = n1
    n4.Parent = n1


    bst.AddKeyValue(10, 10)
    bst.AddKeyValue(9, 9)
    bst.AddKeyValue(11, 11)
    bst.AddKeyValue(14, 14)
    bst.AddKeyValue(13, 13)
    bst.AddKeyValue(15, 15)


    bst.printTree(root)

    print("_____________________________")

    print(bst.DeleteNodeByKey(12))

    bst.printTree(root)

