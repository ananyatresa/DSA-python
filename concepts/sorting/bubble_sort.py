def bubble_sort(nums):
    for i in range(len(nums)):
        swapped = False
        for j in range(1, len(nums)-i):
            if nums[j] < nums[j-1]:
                temp = nums[j]
                nums[j] = nums[j-1]
                nums[j-1] = temp
                swapped = True

        if not swapped:
            break
    return nums

print(bubble_sort([-2,3,2,1,1,1,2,3,4]))