class Node:
    def __init__(self, v):
        self.value = v
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        found_nodes = []
        node = self.head

        while node is not None:
            if node.value == val:
                found_nodes.append(node)
            node = node.next

        if not found_nodes:
            return []
        return found_nodes

    def delete(self, val, all=False):
        node = self.head
        prev = None

        if self.head is None:
            return

        while node and node.value == val:
            self.head = node.next
            node = node.next
            if node is None:
                self.tail = None
            if not all:
                return

        while node is not None:
            if node.value == val:
                prev.next = node.next
                if not all:
                    return
            else:
                prev = node
                self.tail = prev
            node = node.next

    def clean(self):
        while self.head is not None:
            prev = self.head
            self.head = self.head.next
            prev = None
        self.tail = None
        return

    def len(self) -> int:
        node = self.head
        cnt = 0
        while node is not None:
            cnt += 1
            node = node.next
        return cnt

    def insert(self, afterNode, newNode):
        node = self.head

        if self.head is None:
            self.head = newNode
            self.tail = newNode
            return

        if afterNode is None:
            newNode.next = self.head
            self.head = newNode
            return

        while node is not None:
            if node == afterNode:
                newNode.next = afterNode.next
                afterNode.next = newNode
                if newNode.next is None:
                    self.tail = newNode
            node = node.next
        return
