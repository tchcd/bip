class PowerSet:
    def __init__(self):
        self.slots = {}

    def put(self, value):
        self.slots[value] = value

    def size(self):
        return len(self.slots)

    def get(self, value):
        val = self.slots.get(value)
        if val is not None:
            return True
        return False

    def remove(self, value):
        key = self.slots.pop(value, None)
        if key is not None:
            return True
        return False

    def intersection(self, set2):
        res = []
        for el in set2:
            if self.slots.get(el) is not None:
                res.append(el)
        if res:
            return res
        return None

    def union(self, set2):
        first_set = []
        second_set = []

        for el in self.slots.keys():
            if el is not None:
                first_set.append(el)

        for el in set2:
            if self.slots.get(el) is None:
                second_set.append(el)

        union = first_set + second_set

        if union:
            return union
        return None

    def difference(self, set2):
        diff = []
        for el in self.slots.keys():
            if el not in set2:
                diff.append(el)
        if diff:
            return diff
        return None

    def issubset(self, set2):
        for el in set2:
            if self.slots.get(el) is None:
                return False
        return True
