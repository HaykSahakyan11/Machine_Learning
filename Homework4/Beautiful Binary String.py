def beautifulBinaryString(b):
    oo = "010"
    substitutions = 0
    while oo in b:
        index = b.find(oo)
        substitutions += 1
        b = "{}{}{}".format(b[:index + 2], 1, b[index + 3:])
    return print(substitutions)


if __name__ == '__main__':
    n = int(input())

    b = input()

    beautifulBinaryString(b)
