

def power(num: int, pow: int) -> int:
    if pow == 1:
        return num
    return num * power(num, pow - 1)


if __name__ == '__main__':
    print(power(5, 3))
    print(power(2, 4))
