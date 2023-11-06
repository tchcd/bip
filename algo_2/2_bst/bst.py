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


    def compare_keys(self, node: BSTNode, key) -> Optional[BSTFind]:
        if node is None:
            bst = BSTFind()
            bst.Node = None
            bst.NodeHasKey = False
            bst.ToLeft = False
            return bst

        if node.NodeKey == key:
            bst = BSTFind()
            bst.Node = node
            bst.NodeHasKey = True
            bst.ToLeft = False
            return bst

        elif node.NodeKey > key:
            node = node.LeftChild
            return self.compare_keys(node, key)

        elif node.NodeKey < key:
            node = node.RightChild
            return self.compare_keys(node, key)
        else:
            return None

    def AddKeyValue(self, key, val):
        # добавляем ключ-значение в дерево
        return False  # если ключ уже есть

    def FinMinMax(self, FromNode, FindMax):
        # ищем максимальный/минимальный ключ в поддереве
        # возвращается объект типа BSTNode
        return None

    def DeleteNodeByKey(self, key):
        # удаляем узел по ключу
        return False  # если узел не найден

    def Count(self):
        return 0  # количество узлов в дереве

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

    bst.printTree(root)

    print("_____________________________")

    node = bst.FindNodeByKey(11)

    print(node)
    print(node.NodeHasKey)
