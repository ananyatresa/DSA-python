def find_pivot_index(nums):
    start = 0
    end = len(nums) - 1
    while start <= end:
        mid = start + (end - start) // 2
        # CASE 1:  pivot case
        if mid < end and nums[mid] > nums[mid + 1]:
            return mid
        # CASE 2 pivot case
        if mid > start and nums[mid] < nums[mid - 1]:
            return mid - 1
        # CASE 3 non pivot case
        if nums[mid] <= nums[start]:
            end = mid - 1
        else:
            start = mid + 1
    return -1


def binary_search(nums, start, end, target):
    while start <= end:
        mid = start + (end - start) // 2
        if nums[mid] > target:
            end = mid - 1
        elif nums[mid] < target:
            start = mid + 1
        else:
            return mid
    return -1


def search(nums, target) -> int:
    # 1. Find the peak element which is our pivot. 
    pivot = find_pivot_index(nums)
    # 2. Apply BS on LHS and RHS of pivot
    # not rotated
    if pivot == -1:
        return binary_search(nums, 0, len(nums) - 1, target)
    if nums[pivot] == target:
        return pivot
    if target >= nums[0]:
        return binary_search(nums, 0, pivot - 1, target)  # LHS

    return binary_search(nums, pivot + 1, len(nums) - 1, target)  # RHS


print(search([4,5,6,7,0,1,2], 0))
