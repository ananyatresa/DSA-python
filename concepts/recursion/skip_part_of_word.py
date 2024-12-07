def skip(s, word, skip_word):
    if len(s) == 0:
        return ""

    n = len(word)
    m = len(skip_word)
    if s[0:m] == skip_word and s[0:n] != word:
        return skip(s[m:], word, skip_word)
    return s[0] + skip(s[1:], word, skip_word)


s = "appleeappllemango"
word = "apple"
skip_word = "app"
print(skip(s, word, skip_word))
