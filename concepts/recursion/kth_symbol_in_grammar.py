def find_kth_symbol(n, k):
    if n == 1:
        return 0

    # get the mid of current level
    mid = 2 ** n-1 // 2

    if k<=mid:
        # k is in first half of previous level
        return find_kth_symbol(n-1, k)
    else:
        # k is in inverse half(seond half) of previous level
        return 1 - find_kth_symbol(n-1, k-mid)

n=3
k=2
print(find_kth_symbol(n , k))
