def server_load(p, up, memo):
    if len(up) == 0:
        return memo[tuple(p)]

    key = tuple(p)
    if key in memo:
        return memo[key]

    min_load = abs(sum(up) - sum(p))
    memo[key] = min_load


    for i in range(len(up)-1):
        min_load = min(min_load, server_load(p+[up[i]], up[:i] + up[i+1:], memo))

    return min_load

print(server_load([],[1,2,3,4,5], {}))