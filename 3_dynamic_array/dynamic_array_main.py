import ctypes


class DynArray:
    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.array = self.make_array(self.capacity)

    def __len__(self):
        return self.count

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self, i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        return self.array[i]

    def resize(self, new_capacity):
        new_array = self.make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, itm):
        if self.count == self.capacity:
            self.resize(2 * self.capacity)
        self.array[self.count] = itm
        self.count += 1

    def insert(self, i, itm):
        if i < 0 or i > self.count:
            raise IndexError('Index is out of bounds')

        if self.count == self.capacity:
            self.resize(2 * self.capacity)

        new_array = self.make_array(self.capacity)
        for idx in range(self.count+1):
            if idx == i:
                new_array[idx] = itm

            elif idx < i:
                new_array[idx] = self.array[idx]
            else:
                new_array[idx] = self.array[idx-1]

        self.count += 1
        self.array = new_array

    def delete(self, i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')

        if i == 0:
            self.array = self.array[1:self.count]
            self.count = self.count - 1
        else:
            self.array = self.array[:i] + self.array[i+1:self.count]
            self.count = self.count - 1

        if self.count / self.capacity < 0.5:
            self.resize(int(self.capacity / 1.5))
            if self.capacity < 16:
                self.capacity = 16
