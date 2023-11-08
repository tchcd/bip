from typing import Optional


class BSTNode:

    def __init__(self, key, val, parent):
        self.NodeKey = key  # ключ узла
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.LeftChild = None  # левый потомок
        self.RightChild = None  # правый потомок


class BSTFind:  # промежуточный результат поиска

    def __init__(self):
        self.Node = None  # None если
        # в дереве вообще нету узлов

        self.NodeHasKey = False  # True если узел найден
        self.ToLeft = False  # True, если родительскому узлу надо
        # добавить новый узел левым потомком



class BST:

    def __init__(self, node):
        self.Root = node  # корень дерева, или None

    def FindNodeByKey(self, key) -> BSTFind:
        # ищем в дереве узел и сопутствующую информацию по ключу
        if self.Root is None:
            return BSTFind()

        found_node = self.compare_keys(self.Root, key)

        return found_node # возвращает BSTFind

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
        # добавляем ключ-значение в дерево
        bst_find_node = self.FindNodeByKey(key=key)
        if bst_find_node.NodeHasKey:
            return False  # если ключ уже есть

        new_node = BSTNode(key, val, parent=bst_find_node.Node)

        if bst_find_node.ToLeft:
            bst_find_node.Node.LeftChild = new_node
        else:
            bst_find_node.Node.RightChild = new_node


    def FinMinMax(self, FromNode, FindMax: bool) -> BSTNode:
        # ищем максимальный/минимальный ключ в поддереве
        # возвращается объект типа BSTNode
        if FromNode.RightChild and FindMax:
            return self.FinMinMax(FromNode.RightChild, True)
        elif FromNode.LeftChild and not FindMax:
            return self.FinMinMax(FromNode.LeftChild, False)
        else:
            return FromNode


    def DeleteNodeByKey(self, key):
        """
        удаляемый узел надо заменить так называемым узлом-преемником, ключ которого -- наименьший из всех ключей, которые больше ключа удаляемого узла.
        Иными словами, нам надо взять правого потомка удаляемого узла,

        и далее спускаться по всем левым потомкам.
        Если мы находим лист, то его и надо поместить вместо удаляемого узла.
        Если мы находим узел, у которого есть только правый потомок, то преемником берём этот узел,
        а вместо него помещаем его правого потомка.

        """
        node_to_delete = self.FindNodeByKey(key)
        if not node_to_delete.NodeHasKey:
            return False # если узел не найден

        self.delete_traversal(node_to_delete.Node)


        #node_to_replace.Parent = node_to_delete.Node.Parent
        #node_to_replace.LeftChild = node_to_delete.Node.LeftChild
        #node_to_replace.LeftChild =  node_to_delete.Node.RightChild


        #node_to_delete.Node.Parent = None
        #node_to_delete.Node.LeftChild = None
        #node_to_delete.Node.RightChild = None

        a = 5


    def delete_traversal(self, node) -> BSTNode:
        cur_node = node.RightChild
        if cur_node.LeftChild is None and cur_node.RightChild is None:
            cur_node.Parent = node.Parent
            node.Parent.RightChild = cur_node
            node.Parent = None
            node.RightChild = None
            return cur_node
        if cur_node.LeftChild is None and cur_node.RightChild:
            cur_node.RightChild.Parent = node.Parent

            node.Parent = None
            return cur_node.RightChild
        self.delete_traversal(cur_node.RightChild)


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


    bst.AddKeyValue(9,9)
    bst.AddKeyValue(13, 13)


    bst.printTree(root)

    print("_____________________________")

    print(bst.DeleteNodeByKey(12))

    bst.printTree(root)
    #print(bst.FindNodeByKey(9).NodeHasKey)
    #print(bst.FindNodeByKey(13).NodeHasKey)
    #print(bst.FindNodeByKey(11).NodeHasKey)