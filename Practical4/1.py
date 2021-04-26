a_string = input()


def superReducedString(s):
    output = []
    while s:
        char1 = s[0]
        if s.count(char1) % 2 != 0:
            output.append(char1)
        s = s.replace(char1, "")
    if output:
        return output
    return "Empty String"


result = superReducedString(a_string)
print(*result)
