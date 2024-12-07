def skip(s):
    if len(s)==0:
        return ""

    if s[0] == 'a':
        return skip(s[1:])
    return s[0] + skip(s[1:])

s="a"
print(skip(s))
