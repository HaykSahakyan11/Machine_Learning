from collections import Counter


def palindrome_reconstruction(a_word):
    # To count chars and their occurrences
    a_w_counter = Counter(a_word)

    # sorts dictionary to satisfy "lexicographically smallest one" requirement
    sorted_dict = {k: v for k, v in sorted(a_w_counter.items(),
                                           key=lambda item: item[0])}

    # palindrome is the one that is constructed by 2 identity parts
    # (1 is reversed) around a pivot
    # (pivot is any single char including "blank char")
    odds = 0
    odd_char = ""

    # to check whether there is single pivot or not
    for key in sorted_dict.keys():
        if sorted_dict[key] % 2 == 1:
            odds += 1
            odd_char = key

    # if pivot is not single
    if odds > 1:
        print("impossible")
    else:
        a_list, part_1 = [], []

        for key in sorted_dict.keys():
            part_1.extend(key * (sorted_dict[key] // 2))

        a_list.extend(part_1)

        if odd_char:
            a_list.extend(odd_char)

        a_list.extend(part_1[::-1])

        print(*a_list, sep="")


word = input()
palindrome_reconstruction(word)