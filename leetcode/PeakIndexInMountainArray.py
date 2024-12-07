def search(nums):
    start = 0
    end = len(nums) - 1
    while start < end:
        mid = int(start + (end - start) / 2)
        if nums[mid] > nums[mid + 1]:
            end = mid
        else:
            start = mid + 1
    return start #or return end as both will be = and have highest element


nums = [1, 2, 3, 4, 5, 7, 4, 3, 2, 0]
print(search(nums))
