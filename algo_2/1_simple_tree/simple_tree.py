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
        if self.Root is None:
            return []
        all_nodes = []
        self.get_all_nodes_traversal(self.Root, all_nodes)
        return all_nodes

    def get_all_nodes_traversal(self, node, all_nodes):
        all_nodes.append(node)
        for node in node.Children:
            self.get_all_nodes_traversal(node, all_nodes)
        return all_nodes


    def FindNodesByValue(self, val):
        # ваш код поиска узлов по значению
        nodes = self.GetAllNodes()
        return [node for node in nodes if node.NodeValue == val]

    def MoveNode(self, OriginalNode: SimpleTreeNode, NewParent: SimpleTreeNode):
        # ваш код перемещения узла вместе с его поддеревом --
        # в качестве дочернего для узла NewParent
        self.DeleteNode(OriginalNode)
        self.AddChild(NewParent, OriginalNode)

    def Count(self):
        if self.Root is None:
            return 0
        return len(self.GetAllNodes())


    def LeafCount(self):
        if not self.Root:
            return 0

        all_nodes = self.GetAllNodes()
        leafs = [node for node in all_nodes if not node.Children]
        return len(leafs)


    def show_tree_level_with_values(self, break_lvl: Optional[int] = None):
        def traversal(node, level):
            show = f"\t" * level + str(node.NodeValue) + f": level {level}"
            print(show)

            if level == break_lvl:
                return
            for child in node.Children:
                traversal(child, level + 1)
        return traversal(self.Root, 0)
