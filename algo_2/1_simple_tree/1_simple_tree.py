from typing import Optional

class SimpleTreeNode:

    def __init__(self, val, parent):
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.Children = []  # список дочерних узлов

    def __str__(self, level=0):
        ret = "\t" * level + repr(self.NodeValue) + "\n"
        for child in self.Children:
            ret += child.__str__(level + 1)
        return ret

class SimpleTree:
    def __init__(self, root: Optional[SimpleTreeNode]):
        self.Root = root

    def AddChild(self, ParentNode: SimpleTreeNode, NewChild: SimpleTreeNode):
        NewChild.Parent = ParentNode
        ParentNode.Children.append(NewChild)

    def DeleteNode(self, NodeToDelete: SimpleTreeNode):
        if NodeToDelete == self.Root:
            self.Root.Children = []
            self.Root = None
            return

        parent_node = NodeToDelete.Parent
        parent_node.Children.remove(NodeToDelete)

    def GetAllNodes(self):
        # ваш код выдачи всех узлов дерева в определённом порядке
        if not self.Root:
            return []
        nodes = []
        cur_node = self.Root
        def traversal(node):
            nonlocal nodes
            if node.Children:
                nodes.append(node.NodeValue)
                for node in node.Children:
                    traversal(node)
        traversal(cur_node)
        return nodes

    def FindNodesByValue(self, val):
        # ваш код поиска узлов по значению
        nodes = []
        cur_node = self.Root
        def traversal(node):
            if node.NodeValue == val and node.Children:
                nodes.append(node)
            for node in node.Children:
                traversal(node)
        traversal(cur_node)
        return nodes

    def MoveNode(self, OriginalNode: SimpleTreeNode, NewParent: SimpleTreeNode):
        # ваш код перемещения узла вместе с его поддеревом --
        # в качестве дочернего для узла NewParent
        pass

    def Count(self):
        """исправить на кол-во вместо списка"""
        cnt = []
        if not self.Root:
            return 0
        cur_node = self.Root
        def traversal(node: SimpleTreeNode):
            nonlocal cnt
            if node.Children:
                cnt.append(node.NodeValue)
                for children_node in node.Children:
                    traversal(children_node)
            return cnt
        return traversal(cur_node)


    def LeafCount(self):
        """исправить на кол-во вместо списка"""
        cnt = []
        if not self.Root:
            return 0
        cur_node = self.Root

        def traversal(node: SimpleTreeNode):
            nonlocal cnt
            if node.Children:
                for children_node in node.Children:
                    traversal(children_node)
            else:
                cnt.append(node.NodeValue)
            return cnt

        return traversal(cur_node)


if __name__ == '__main__':
    root = SimpleTreeNode(val=0, parent=None)
    n1 = SimpleTreeNode(val=1, parent=None)
    n2 = SimpleTreeNode(val=2, parent=None)
    n22 = SimpleTreeNode(val=2, parent=None)
    n3 = SimpleTreeNode(val=3, parent=None)
    n4 = SimpleTreeNode(val=4, parent=None)
    n5 = SimpleTreeNode(val=5, parent=None)

    tree = SimpleTree(root=root)
    #############################################
    tree.AddChild(ParentNode=root, NewChild=n2)
    #tree.AddChild(ParentNode=n2, NewChild=n1)
    tree.AddChild(ParentNode=root, NewChild=n3)
    tree.AddChild(ParentNode=n2, NewChild=n4)
    tree.AddChild(ParentNode=n3, NewChild=n22)
    tree.AddChild(ParentNode=n22, NewChild=n5)

    #print(tree.LeafCount())
    print(root)

    #tree.DeleteNode(n1)
    print(tree.FindNodesByValue(2))
    #print(root)