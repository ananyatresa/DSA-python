def search(nums, target):
    start = len(nums) - 1
    end = 0
    while start >= end:
        mid = (start + end) // 2
        if target > nums[mid]:
            start = mid - 1
        elif target < nums[mid]:
            end = mid + 1
        else:
            return mid
    return -1


nums = [10, 9, 8, 7, 6, 5]
target = 6
print(search(nums, target))
