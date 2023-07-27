class NativeCache:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size
        self.hits = [0] * self.size

    def hash(self, val):
        slot = sum([ord(v) for v in val]) % self.size
        return slot

    def step(self, slot):
        step = 1
        if self.size % 2:
            step = 2
        slot = (slot + step) % self.size
        return slot

    def add_item(self, key, value):
        slot = self.hash(key)
        for attempt in range(self.size):
            if self.slots[slot] is None:
                self.slots[slot] = key
                self.values[slot] = value
                return
            slot = self.step(slot)

        slot_to_replace = self.get_kicked_slot()
        self.slots[slot_to_replace] = key
        self.values[slot_to_replace] = value

    def get_value(self, key):
        slot = self.hash(key)
        for attempt in range(self.size):
            if self.slots[slot] == key:
                self.hits[slot] += 1
                return self.values[slot]
            slot = self.step(slot)
        return None

    def get_kicked_slot(self):
        min_hits = min(self.hits)
        return self.hits.index(min_hits)
