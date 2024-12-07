def permutations(p, up):
    if len(up) == 0:
        return 1

    ch = up[0]
    c = 0
    for i in range(len(p)+1):
        first = p[0:i]
        second = p[i:]
        c += permutations(first+ch+second, up[1:])

    return c


str="abcd"
print(permutations("",str))