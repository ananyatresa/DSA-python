def find_ans(nums, target):
    start = 0
    end = 1
    while target > nums[end]:
        newStart = end + 1
        end = end + (end - start + 1) * 2
        start = newStart
    return search(nums, target, start, end)


def search(nums, target, start, end):
    while start < end:
        mid = int((start + (end - start)) / 2)
        if target > nums[mid]:
            start = mid + 1
        elif target < nums[mid]:
            end = mid - 1
        else:
            return mid
    return -1


nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 18, 20, 25, 28, 34, 39, 45, 47, 51]
target = 13
print(find_ans(nums, target))
