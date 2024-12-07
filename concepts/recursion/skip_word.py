def skip(s, word):
    if len(s) == 0:
        return ""

    n = len(word)
    if s[0:n] == word:
        return skip(s[n:], word)
    return s[0] + skip(s[1:], word)


s = "abccddeeffggabcd"
word = "abcd"
print(skip(s, word))
