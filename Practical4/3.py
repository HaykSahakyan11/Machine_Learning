s2 = "SHINCHAN"  # input()
s1 = "NOHARAAA"  # input()


# if str_1[0] in str_2:
#    pass
# else:
#    pass


# index_1, index_2 = 0 , 0

def commonChild(s1, s2):
    output_1, output_2 = [], []
    str_1 , str_2 = s1, s2
    mutated = False

    while s1:
        print(s1)
        char_1 = s1[0]
        if char_1 in s2:
            index_2 = s2.find(char_1)
            output_1.append(char_1)
            s2 = s2[index_2 + 1:]
        s1 = s1[1:]
    while s1:
        print(s1)
        char_1 = s1[0]
        if char_1 in s2:
            index_2 = s2.find(char_1)
            output_1.append(char_1)
            s2 = s2[index_2 + 1:]
        s1 = s1[1:]

    print(output_1)
    return len(output_1)


print(s1)
print(commonChild(s1, s2))
