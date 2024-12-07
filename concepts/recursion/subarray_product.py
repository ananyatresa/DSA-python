def product(arr, k):
    total = 1
    for num in arr:
        total *= num
    if total < k:
        return [arr]
    return []


def subset(p, up, k):
    if len(up) == 0:
        return product(p, k)

    # Take 1
    arr = subset(p + [up[0]], up[1:], k)

    # Ignore 1
    arr.extend(subset(p, up[1:], k))

    return arr

print(subset([],[10,5,2,6],100))