from typing import Optional

class BSTNode:

    def __init__(self, key, val, parent):
        self.NodeKey = key
        self.NodeValue = val
        self.Parent = parent
        self.LeftChild = None
        self.RightChild = None


class BSTFind:
    def __init__(self):
        self.Node = None
        self.NodeHasKey = False
        self.ToLeft = False


class BST:

    def __init__(self, node):
        self.Root = node

    def FindNodeByKey(self, key) -> BSTFind:
        if self.Root is None:
            return BSTFind()

        found_node = self.compare_keys(self.Root, key)

        return found_node

    def create_bst_find_node(self, node: Optional[BSTNode]= None, node_has_key: bool = False, to_left: bool = False):
        bst = BSTFind()
        bst.Node = node
        bst.NodeHasKey = node_has_key
        bst.ToLeft = to_left
        return bst

    def compare_keys(self, node: BSTNode, key) -> Optional[BSTFind]:
        if node.NodeKey == key:
            return self.create_bst_find_node(node, node_has_key=True)

        elif node.NodeKey > key:
            if node.LeftChild is None:
                return self.create_bst_find_node(node, node_has_key=False, to_left=True)
            node = node.LeftChild
            return self.compare_keys(node, key)

        elif node.NodeKey < key:
            if node.RightChild is None:
                return self.create_bst_find_node(node, node_has_key=False, to_left=False)
            node = node.RightChild
            return self.compare_keys(node, key)
        else:
            return None

    def AddKeyValue(self, key, val):
        if self.Root is None:
            self.Root = BSTNode(key, val, None)
            return True

        bst_find_node = self.FindNodeByKey(key=key)
        if bst_find_node.NodeHasKey:
            return False

        new_node = BSTNode(key, val, parent=bst_find_node.Node)

        if bst_find_node.ToLeft:
            bst_find_node.Node.LeftChild = new_node
        else:
            bst_find_node.Node.RightChild = new_node
        return True


    def FinMinMax(self, FromNode, FindMax):
        if FindMax:
            node = self.find_max(FromNode, FromNode.Parent)
        else:
            node = self.find_min(FromNode, FromNode.Parent)
        return node

    def find_max(self, node, parent):
        if not node:
            return parent
        return self.find_max(node.RightChild, node)

    def find_min(self, node, parent):
        if not node:
            return parent
        return self.find_min(node.LeftChild, node)


    def DeleteNodeByKey(self, key):
        node_to_delete = self.FindNodeByKey(key)
        if not node_to_delete.NodeHasKey:
            return False

        node_to_delete = node_to_delete.Node
        delete_left_node = node_to_delete.LeftChild
        delete_right_node = node_to_delete.RightChild

        if node_to_delete == self.Root:
            self.Root = None

        node_to_replace = self.node_to_replace_traversal(delete_left_node, delete_right_node)

        if delete_left_node and delete_right_node:
            self.replace_nodes(node_to_delete, delete_left_node, delete_right_node, node_to_replace)

        if node_to_replace:
            node_to_replace.Parent = node_to_delete.Parent
        if not node_to_delete.Parent:
            self.Root = node_to_replace
            return True
        if node_to_delete.NodeKey > node_to_delete.Parent.NodeKey:
            node_to_delete.Parent.RightChild = node_to_replace
        if node_to_delete.NodeKey < node_to_delete.Parent.NodeKey:
            node_to_delete.Parent.LeftChild = node_to_replace
        return True

    def replace_nodes(self, node_to_delete, left_child, right_child, node_to_replace):
        left_child.Parent = node_to_replace
        node_to_replace.LeftChild = left_child
        if node_to_replace == node_to_delete.RightChild:
            return
        if node_to_replace.RightChild:
            parent = node_to_replace.Parent
            parent.LeftChild = node_to_replace.RightChild
        else:
            node_to_replace.Parent.LeftChild = None
        node_to_replace.RightChild = right_child
        right_child.Parent = node_to_replace


    def node_to_replace_traversal(self, left_child, right_child):
        if not left_child and not right_child:
            return None
        if not left_child and right_child:
            return right_child
        if left_child and not right_child:
            return left_child
        if left_child and right_child:
            min_node = self.FinMinMax(right_child, False)
            return min_node


    def Count(self):
        if not self.Root:
            return 0
        nodes = []
        def traversal(node: BSTNode):
            if node:
                traversal(node.LeftChild)
                traversal(node.RightChild)
                nodes.append(node)

        traversal(self.Root)
        return len(nodes)

    def WideAllNodes(self):


        pass


    def DeepAllNodes(self, order):
        """
        находясь в некотором узле, мы проверяем на наличие искомого объекта, в некотором порядке,
        левое поддерево (рекурсивно), текущий узел, правое поддерево (рекурсивно).
        (in-order)
        """
        all_nodes = []
        match order:
            case 0:
                return self.in_order_traversal(self.Root, all_nodes)
            case 1:
                order = "post-order"
            case 2:
                order = "pre-order"

        pass

    # 4,2,6,12,10,9
    # 2,6,4,9,11,10
    def in_order_traversal(self, node: BSTNode, all_nodes: list):
        if node.LeftChild:
            all_nodes.append(node.LeftChild.NodeKey)  # Убрать Key оставит ьноду
            self.in_order_traversal(node.LeftChild, all_nodes)
        if node.RightChild:
            all_nodes.append(node.RightChild.NodeKey)  # Убрать Key оставит ьноду
            self.in_order_traversal(node.RightChild, all_nodes)
        all_nodes.append(node.NodeKey)


    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.LeftChild, level + 1)
            print(' ' * 4 * level + '-> ' + str(node.NodeKey))
            self.printTree(node.RightChild, level + 1)



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

    print(bst.DeepAllNodes(0))