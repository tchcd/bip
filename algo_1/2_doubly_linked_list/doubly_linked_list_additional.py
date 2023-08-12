"""
Фиктивный узел позволяет избавиться от этих краевых ситуаций,
оставив только по одной универсальной операции на добавление и удаление.
Идея в том, что мы добавляем в список два искусственных узла -- голову и хвост,
которые пользователю класса не видны (они отличаются от видимых узлов, например, булевым флажком,
а лучше всего это делать через наследование и перегрузку). Теперь, добавляя или удаляя узлы,
мы всегда будем уверены, что у каждого из них имеется и предыдущий узел, и последующий,
и от дополнительных проверок и модификаций полей head и tail можно избавиться.
"""

class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

    def __str__(self):
        return str(self.value)


class DummyHead(Node):
    def __init__(self):
        super().__init__(False)

class DummyTail(Node):
    def __init__(self):
        super().__init__(False)


class DummyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.dummy_head = DummyHead()
        self.dummy_tail = DummyTail()

    def add_to_tail(self, item):
        if self.head is None:
            self.head = item
            #item.prev = self.dummy_head
            #item.next = self.dummy_tail
        else:
            self.tail.next = item
            item.prev = self.tail
            #item.next = self.dummy_tail
        self.tail = item
        self.tail.next = self.dummy_tail
        self.head.prev = self.dummy_head

    def print_all_nodes(self):
        node = self.head
        while node and not isinstance(node, DummyTail):
            print('Текущая нода', node)
            print('Предыдущая нода', node.prev)
            print('Следующая нода', node.next)
            print('____________', )

            node = node.next

    def delete(self, val, all=False):
        node = self.head
        prev = self.head.prev

        while node and not isinstance(node, DummyTail):
            if node.value == val:
                prev.next = node.next
                node.next.prev = prev
            else:
                prev = node
            node = node.next


if __name__ == '__main__':
    ll = DummyLinkedList()
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)

    ll.add_to_tail(node1)
    ll.add_to_tail(node2)
    ll.add_to_tail(node3)

    ll.delete(1)
    ll.print_all_nodes()
