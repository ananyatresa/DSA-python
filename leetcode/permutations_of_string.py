def permutations(p, up):
    if len(up) == 0:
        return [p] if p != "" else []

    # take each character
    ch = up[0]
    arr = []

    # Put it in p+1 positions of p and call recursively
    for i in range(len(p) + 1):
        first = p[0:i]
        second = p[i:]
        arr.extend(permutations(first + ch + second, up[1:]))

    return arr


str = 'abc'
print(permutations("", str))
