def subset(p, up, target, curr_sum):
    if curr_sum == target:
        return [p]

    if curr_sum > target or not up:
        return []

    # Take old element recursively // 2 2 2
    arr = subset(p + [up[0]], up, target, curr_sum + up[0])

    # Take new element recursively // 2 2 3
    arr.extend(subset(p, up[1:], target, curr_sum))
    return arr


s = [2,3]
target=9
print(subset([], s, target,0))


















# def subset(p, up, target):
#     if len(up) == 0:
#         return p if sum(p) == target else []
#
#     # Add new
#     arr = subset(p + [up[0]], up[1:], target)
#
#     # Take Old
#     arr.extend(subset(p+[p[-1]], up[1:], target))
#
#     return arr
#
#
# s = [2,3,5]
# target=8
# print(subset([], s, target))
