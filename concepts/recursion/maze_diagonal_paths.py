def return_paths(p, r, c):
    if r == 1 and c == 1:
        return [p]

    arr = []
    if r > 1:
        arr = return_paths(p + 'V', r - 1, c)
    if r > 1 and c > 1:
        arr.extend(return_paths(p + 'D', r - 1, c - 1))
    if c > 1:
        arr.extend(return_paths(p + 'H', r, c - 1))

    return arr


row = 3
column = 3
print(return_paths("", row, column))
