def remove(s):
    if len(s) < 2:
        return s

    if s[0] != s[1]:
        return s[0] + remove(s[1:])
    return remove(s[1:])


print(remove("aabb"))
