def wave_sort(nums):
    for i in range(0, len(nums), 2):
        if i > 0 and nums[i-1] > nums[i]:
            nums[i-1], nums[i] = nums[i], nums[i-1]
        if i < len(nums)-1 and nums[i + 1] > nums[i]:
            nums[i + 1], nums[i] = nums[i], nums[i + 1]

    return nums


print(wave_sort([10, 5, 6, 3, 2, 20, 100, 80]))



# o(nlogn) approach
# def wave_sort(nums):
#     nums.sort()
#
#     for i in range(1,len(nums), 2):
#         temp = nums[i]
#         nums[i] = nums[i-1]
#         nums[i-1] = temp
#
#     return nums


