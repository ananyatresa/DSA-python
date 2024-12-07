def dice_throw(p, up, target):
    if sum(p) == target:
        return [p]

    if sum(p) > target or not up:
        return []

    # Take old element recursively // 2 2 2
    arr = dice_throw(p + [up[0]], up, target)

    # Take new element recursively // 2 2 3
    arr.extend(dice_throw(p, up[1:], target))
    return arr

target=4
print(dice_throw([], [1,2,3,4,5,6], target))






# def dice_throw(p, target, k):
#     if target == 0:
#         return [p]
#
#     arr = []
#     for j in range(n):
#         for i in range(1, k+1):
#             if i <= target:
#                 arr.extend(dice_throw(p + [i], target-i, k))
#
#     return arr
#
#
# target = 4
# k=6
# n=2
# print(dice_throw([], target, k))
