def cyclic_sort(nums):
    i = 0
    while i < len(nums):
        if nums[i] != nums[nums[i] - 1]:
            temp = nums[i]
            nums[i] = nums[temp - 1]
            nums[temp - 1] = temp
        else:
            i += 1
    return nums


print(cyclic_sort([2,4,3,1,1,1,2,2,4,3,2]))


# for negative -1 to -n
# def cyclic_sort(nums):
#     i = 0
#     while i < len(nums):
#         if nums[i] != nums[abs(nums[i]) - 1]:
#             temp = nums[i]
#             nums[i] = nums[abs(temp) - 1]
#             nums[abs(temp) - 1] = temp
#         else:
#             i += 1
#     return nums
#
#
# print(cyclic_sort([-2,-3,-1,-1,-2]))

