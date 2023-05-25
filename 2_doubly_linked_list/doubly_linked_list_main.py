from typing import Union, List, Optional


class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item: Node):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node:
            print(node.value)
            node = node.next

    def find(self, val: Union[int, float, str, bool]) -> Union[Node, None]:
        node = self.head
        while node:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val: Union[int, float, str, bool]) -> Union[List[Node], None]:
        node = self.head
        found_elements = []
        while node:
            if node.value == val:
                found_elements.append(node)
            node = node.next
        return found_elements

    def delete(self, val, all=False) -> None:
        node = self.head
        prev = None
        flag = 0

        if self.head is None:
            return

        while node and node.value == val:
            self.head = node.next
            node = node.next
            if node is None:
                self.tail = None
            if not all:
                return

        while node:
            if node.value == val and not flag:
                prev.next = node.next
                if not all:
                    flag = 1
            else:
                prev = node
                self.tail = prev
            node = node.next


    def clean(self) -> None:
        self.__init__()

    def len(self) -> int:
        node = self.head
        c = 0
        while node:
            c += 1
            node = node.next
        return c

    def insert(self, afterNode, newNode):
        node = self.head

        if afterNode is None and self.head is None:
            self.head = newNode
            self.tail = newNode

        if afterNode is None and self.head:
            while node:
                if node.next is None:
                    node.next = newNode
                    self.tail = newNode
                    newNode.next = None

                node = node.next
            self.head = newNode
            self.tail = newNode

        while node:
            if node == afterNode:
                newNode.next = afterNode.next
                afterNode.next = newNode
                if newNode.next is None:
                    self.tail = newNode
            node = node.next

# я совершенно забыл следить еще и за prev у каждого объекта
    def add_in_head(self, newNode):
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            return

        node = self.head
        newNode.next = node
        self.head = newNode


if __name__ == "__main__":
    ll = LinkedList2()
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(2)
    ll.add_in_tail(node1)
    ll.add_in_tail(node2)
    ll.add_in_tail(node3)

    ll.delete(2)
    ll.print_all_nodes()
    print('head', ll.head)
    print('tail', ll.tail)



