def get_length(input_list: list, num=0):
    if not input_list:
        return num
    input_list.pop()
    return get_length(input_list, num + 1)


def get_closure_length(input_list: list):
    """
    Вариант с замыканием, чтобы избавиться от передачи дополнительного
    аргумента-счетчика и скрыть его во внутренней функции
    """
    def inner(num):
        # тут так же желательно создать копию списка, чтобы не изменять входящий
        if not input_list:
            return num
        input_list.pop()
        return inner(num + 1)
    return inner(0)


if __name__ == '__main__':
    print(get_length([1, 1, 1, 1]))         # 4
    print(get_closure_length([1, 1, 1]))    # 3
    print(get_closure_length([]))           # 0


