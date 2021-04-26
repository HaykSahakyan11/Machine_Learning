from collections import Counter


def countCharacters(words, chars: str) -> int:
    out = 0
    for word in words:  # cat
        for char in word:  # c,a,t
            if word.count(char) > chars.count(char):
                break
        else:
            out += len(word)
    return out


def countCharacters_my_version(words, chars) -> int:
    chars_dict = Counter(chars)
    output = 0
    for word in words:
        dict_word = Counter(word)
        for char in word:
            if dict_word[char] > chars_dict[char]:
                break
        else:
            output += len(word)
    return output


a_words = ["cat", "bt", "hat", "tree"]
chars = "atach"

print(countCharacters(a_words, chars))
