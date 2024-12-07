def subset(p, up):
    if len(up) == 0:
        return [p] if p != "" else []


    # Take it
    arr = subset(p + up[0], up[1:])

    # Ignore it
    arr.extend(subset(p, up[1:]))

    return arr


s = "abc"
print(subset("", s))
