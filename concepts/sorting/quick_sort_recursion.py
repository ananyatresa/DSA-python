def quick_sort(nums, low, hi):
    if low >= hi:
        return

    start = low
    end = hi
    mid = (start + end) // 2  # Select middle as pivot
    pivot = nums[mid]

    # Put pivot in correct position
    while start <= end:
        while nums[start] < pivot:
            start += 1
        while nums[end] > pivot:
            end -= 1

        # Swap on finding violation
        if start <= end:
            temp = nums[start]
            nums[start] = nums[end]
            nums[end] = temp
            start += 1  # Updated start and end to reflect next indices
            end -= 1

    # Sort both halves recursively
    quick_sort(nums, low, end)
    quick_sort(nums, start, hi)


nums = [2, 1, 5, 4]
quick_sort(nums, 0, len(nums)-1)
print(nums)
