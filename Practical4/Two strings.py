def twoStrings(s1, s2):
    return ("Yes", "No")[set(s1).intersection(set(s2)) == set()]


if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)
        print(result)
