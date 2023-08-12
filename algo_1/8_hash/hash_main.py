class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def hash_fun(self, value):
        slot = sum([ord(i) for i in value]) % self.size
        return slot

    def seek_slot(self, value):
        slot = self.hash_fun(value)

        for _ in range(len(self.slots)):
            if not self.slots[slot]:
                return slot
            else:
                slot += self.step
                slot = slot % self.size
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
            else:
                slot += self.step
                slot = slot % self.size
        return None



