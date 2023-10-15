
def sum_of_nums(d: int) -> int:
    if d < 10:
        return d
    d, m = divmod(d, 10)
    return m + sum_of_nums(d)


if __name__ == '__main__':
    print(sum_of_nums(123))
    print(sum_of_nums(234))