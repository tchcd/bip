class PowerSet:
    def __init__(self):
        self.slots = {}

    def put(self, value) -> None:
        self.slots[value] = value

    def size(self) -> int:
        return len(self.slots)

    def get(self, value) -> bool:
        val = self.slots.get(value)
        if val is not None:
            return True
        return False

    def remove(self, value) -> bool:
        key = self.slots.pop(value, None)
        if key is not None:
            return True
        return False

    def intersection(self, set2):
        intersection = PowerSet()
        for el in set2.slots.values():
            if self.slots.get(el) is not None:
                intersection.put(el)
        return intersection

    def union(self, set2):
        union = PowerSet()

        for el in self.slots.keys():
            union.put(el)

        for el in set2.slots.values():
            if self.slots.get(el) is None:
                union.put(el)
        return union

    def difference(self, set2):
        diff = PowerSet()
        for el in self.slots.keys():
            if el not in set2.slots:
                diff.put(el)
        return diff

    def issubset(self, set2) -> bool:
        for el in set2.slots.values():
            if self.slots.get(el) is None:
                return False
        return True
