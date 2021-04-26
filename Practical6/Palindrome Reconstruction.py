def palindrome_reconstruction(s):
    freq = {}
    for sym in s:
        freq[sym] = freq.get(sym, 0) + 1

    mid = ''
    for (sym, count) in freq.items():
        if count % 2 == 1:
            if mid:
                return 'impossible'
            mid = sym

    palindrome = ''
    for sym in sorted(freq.keys()):
        palindrome += sym * (freq[sym] // 2)

    return palindrome + mid + palindrome[::-1]
