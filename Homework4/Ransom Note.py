def checkMagazine(magazine, note):
    for word in note:
        if word in magazine:
            magazine.remove(word)
        else:
            return print("No")
    return print("Yes")


if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
