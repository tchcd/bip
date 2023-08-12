
class BloomFilter:
    def __init__(self, f_len):
        self.filter_len = f_len
        self.bit_array = 0b0 * f_len

    def hash1(self, str1):
        random_num = 17
        cur = 0
        for c in str1:
            code = ord(c)
            cur = (cur * random_num + code) % self.filter_len
        return cur

    def hash2(self, str1):
        random_num = 223
        cur = 0
        for c in str1:
            code = ord(c)
            cur = (cur * random_num + code) % self.filter_len
        return cur

    def add(self, str1):
        hash1 = self.hash1(str1)
        hash2 = self.hash2(str1)
        mask1 = 1 << hash1
        mask2 = 1 << hash2
        self.bit_array = self.bit_array | mask1
        self.bit_array = self.bit_array | mask2
        return self.bit_array

    def is_value(self, str1):
        check_arr = 0b0
        hash1 = self.hash1(str1)
        hash2 = self.hash2(str1)
        check_mask1 = 1 << hash1
        check_mask2 = 1 << hash2
        check_arr = check_arr | check_mask1
        check_arr = check_arr | check_mask2
        return self.bit_array & check_arr == check_arr

