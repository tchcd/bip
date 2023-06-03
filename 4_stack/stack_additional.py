def postfix_operation(s: str):
    s1 = []
    s2 = []
    data = s.split()

    for i in data:
        s1.append(i)

    operations = {
        '*': lambda a, b: a * b,
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '/': lambda a, b: a / b,
    }

    for el in s1:
        if el == '=':
            return s2[0]
        if el.isnumeric():
            s2.append(el)
        else:
            first = int(s2.pop())
            second = int(s2.pop())
            try:
                fn = operations[el]
                res = fn(first, second)
                s2.append(res)
            except KeyError:
                raise


if __name__ == "__main__":
    print(postfix_operation('1 2 % 3 * ='))
    print(postfix_operation('8 2 + 5 * 9 + ='))
