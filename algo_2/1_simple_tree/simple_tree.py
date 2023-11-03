from typing import Optional

class SimpleTreeNode:

    def __init__(self, val, parent):
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.Children = []  # список дочерних узлов


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
        cur_node = self.Root
        nodes = self.get_all_nodes_traversal(cur_node)
        return nodes

    def get_all_nodes_traversal(self, node):
        nodes = []
        if node.Children:
            nodes.append(node)
            for node in node.Children:
                nodes.extend(self.get_all_nodes_traversal(node))
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
        self.DeleteNode(OriginalNode)
        self.AddChild(NewParent, OriginalNode)

    def Count(self):
        cnt = 0
        if not self.Root:
            return 0
        cur_node = self.Root

        def traversal(node: SimpleTreeNode):
            nonlocal cnt
            if node.Children:
                cnt += 1
            for children_node in node.Children:
                traversal(children_node)
            return cnt
        return traversal(cur_node)


    def LeafCount(self):
        cnt = 0
        if not self.Root:
            return 0
        cur_node = self.Root

        def traversal(node: SimpleTreeNode):
            nonlocal cnt
            if not node.Children:
                cnt += 1
            for children_node in node.Children:
                traversal(children_node)
            return cnt
        return traversal(cur_node)


    def get_tree_level_with_values(self, node, break_lvl: Optional[int] = None):
        def traversal(node, level):
            show = f"\t" * level + str(node.NodeValue) + f": level {level}"
            print(show)

            if level == break_lvl:
                return
            for child in node.Children:
                traversal(child, level + 1)
        return traversal(node, 0)
