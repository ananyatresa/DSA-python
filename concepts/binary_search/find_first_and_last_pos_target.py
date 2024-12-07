# we apply bs twice. both on full array where we try to find firstoccurrence and then again to find last_occurrnec
def search(nums, target,find_first_occurrence):
    ans = -1
    start = 0
    end = len(nums)-1
    while start <= end:
        mid = (start+end) // 2
        if target > nums[mid]:
            start = mid + 1
        elif target < nums[mid]:
            end = mid - 1
        else:
            ans = mid
            if find_first_occurrence:
                end = mid - 1
            else:
                start = mid + 1
    return ans


def find_position(nums, target):
    result = [-1,-1]
    result[0] = search(nums, target, True)
    if result[0] != -1:
        result[1] = search(nums, target, False)


nums = [5, 7, 7, 7, 7, 8, 8, 10]
target = 7
print(find_position(nums, target))
