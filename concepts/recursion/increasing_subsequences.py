def find_subseq(p, up):
    if len(up) == 0:
        return [p] if len(p) >= 2 else []

    arr = []
    if len(p) == 0 or p[-1] <= up[0]:
        # Take 1
        arr = find_subseq(p+[up[0]], up[1:])

    # Ignore 1
    arr.extend(find_subseq(p, up[1:]))


    return arr



sets = set(tuple(seq) for seq in find_subseq([], [4,6,7,7]))
result = [list(seq) for seq in sets]

# print(find_subseq([], [4,6,7,7]))

print(result)