class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class OrderedList:
    def __init__(self, asc: bool):
        self.head = None
        self.tail = None
        self.__ascending = asc

    def compare(self, v1, v2):
        if v1 < v2:
            return -1
        if v1 > v2:
            return 1
        return 0

    def add_to_asc(self, new_node):
        cur_node = self.head
        if self.compare(cur_node.value, new_node.value) == 1:
            self.head = new_node
            new_node.next = cur_node
            cur_node.prev = new_node
            return

        while cur_node:
            res = self.compare(cur_node.value, new_node.value)
            if res == 1 and self.__ascending:
                new_node.prev = cur_node.prev
                new_node.next = cur_node
                cur_node.prev.next = new_node
                cur_node.prev = new_node
                return
            if not cur_node.next:
                cur_node.next = new_node
                new_node.prev = cur_node
                self.tail = new_node
                return
            cur_node = cur_node.next

    def add_to_desc(self, new_node):
        cur_node = self.head
        if self.compare(cur_node.value, new_node.value) == -1:
            self.head = new_node
            new_node.next = cur_node
            cur_node.prev = new_node
            return

        while cur_node:
            res = self.compare(cur_node.value, new_node.value)
            if res == -1 and not self.__ascending:
                new_node.prev = cur_node.prev
                new_node.next = cur_node
                cur_node.prev.next = new_node
                cur_node.prev = new_node
                return
            if not cur_node.next:
                cur_node.next = new_node
                new_node.prev = cur_node
                self.tail = new_node
                return
            cur_node = cur_node.next

    def add(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        if self.__ascending:
            self.add_to_asc(new_node)
        else:
            self.add_to_desc(new_node)

    def find(self, val):
        """Time complexity O(n)"""
        cur_node = self.head

        while cur_node:
            res = self.compare(cur_node.value, val)
            if res == 0:
                return cur_node
            if res == 1 and self.__ascending:
                return None
            if res == -1 and not self.__ascending:
                return None
            cur_node = cur_node.next

    def delete(self, val):
        cur_node = self.head
        prev = None
        removed = False

        if self.head is None:
            return

        while cur_node and cur_node.value == val:
            self.head = cur_node.next
            cur_node = cur_node.next
            if cur_node is None:
                self.tail = None
            else:
                cur_node.prev = None

        while cur_node:
            if cur_node.value == val and not removed:
                prev.next = cur_node.next
                removed = True
            else:
                cur_node.prev = prev
                prev = cur_node
                self.tail = prev
            cur_node = cur_node.next

    def clean(self, asc):
        self.__init__(asc)

    def len(self):
        c = 0
        node = self.head
        while node != None:
            c += 1
            node = node.next
        return c

    def get_all(self):
        r = []
        node = self.head
        while node != None:
            r.append(node)
            node = node.next
        return r


class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1, v2):
        v1 = v1.strip()
        v2 = v2.strip()
        if v1 < v2:
            return -1
        if v1 > v2:
            return 1
        return 0
