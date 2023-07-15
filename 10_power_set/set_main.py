class HashTable:
    def __init__(self, sz, stp):
        self.set_size = sz
        self.step = stp
        self.slots = [None] * self.set_size

    def hash_fun(self, value):
        slot = sum([ord(i) for i in value]) % self.set_size
        return slot

    def seek_slot(self, value):
        slot = self.hash_fun(value)

        for _ in range(len(self.slots)):
            if self.slots[slot] == value:
                return None
            if self.slots[slot] is None:
                return slot
            slot += self.step
            slot = slot % self.set_size
        return None

    def put(self, value):
        slot = self.seek_slot(value)
        if slot is not None:
            self.slots[slot] = value
            return slot
        return None

    def find(self, value):
        slot = self.hash_fun(value)

        for _ in range(len(self.slots)):
            if self.slots[slot] == value:
                return slot
            slot += self.step
            slot = slot % self.set_size
        return None


class PowerSet(HashTable):
    def __init__(self, sz, stp):
        super().__init__(sz, stp)

    def size(self):
        return len(self.slots)

    def get(self, value):
        slot = self.hash_fun(value)
        for _ in range(len(self.slots)):
            if self.slots[slot] == value:
                return True
            slot += self.step
            slot = slot % self.set_size
        return False

    def remove(self, value):
        slot = self.hash_fun(value)
        for _ in range(len(self.slots)):
            if self.slots[slot] == value:
                self.slots[slot] = None
                return True
            slot += self.step
            slot = slot % self.set_size
        return False

    def intersection(self, set2):
        res = []
        for el in set2:
            element_slot = self.find(el)
            if element_slot is not None:
                res.append(el)
        if res:
            return res
        return None

    def union(self, set2):
        first_set = []
        second_set = []

        for el in self.slots:
            if el is not None:
                first_set.append(el)

        for el in set2:
            if not self.find(el):
                second_set.append(el)

        union = first_set + second_set

        if union:
            return union
        return None

    def difference(self, set2):
        diff = []
        for el in self.slots:
            if el is not None and el not in set2:
                diff.append(el)
        if diff:
            return diff
        return None

    def issubset(self, set2):
        for el in set2:
            if not self.find(el):
                return False
        return True

