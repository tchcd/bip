class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.step = 1
        self.slots = [None] * self.size
        self.values = [None] * self.size

    def hash_fun(self, key: str) -> int:
        slot = sum([ord(i) for i in key]) % self.size
        return slot

    def seek_slot(self, key):
        slot = self.hash_fun(key)
        for _ in range(self.size):
            if self.values[slot] == key:
                return slot
            slot += self.step
            slot = slot % self.size
        return None

    def is_key(self, key):
        if self.seek_slot(key) is not None:
            return True
        return False

    def put(self, key, value):
        slot = self.hash_fun(key)
        for _ in range(self.size):
            if self.values[slot] is None:
                self.values[slot] = key
                self.slots[slot] = value
                return slot
            slot += self.step
            slot = slot % self.size
        return None

    def get(self, key):
        slot = self.hash_fun(key)
        if self.seek_slot(key) is not None:
            return self.slots[slot]
        return None
