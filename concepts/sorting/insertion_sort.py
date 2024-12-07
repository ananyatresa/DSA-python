# compare curr with all prev and keep swapping till each element is placed in its correct position

def insertion_sort(nums):
    for i in range(len(nums)-1):
        j = i+1
        while j>0:
            if nums[j] < nums[j-1]:
                temp = nums[j]
                nums[j] = nums[j-1]
                nums[j-1] = temp
            else:
                break
            j-=1
    return nums

print(insertion_sort([-3,-2,-1,1,10,2,45,8,2]))