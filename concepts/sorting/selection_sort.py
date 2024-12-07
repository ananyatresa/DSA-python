# In each iteration, select and swap the maximum element in arr with last element. Decrement the arr length too

def find_max(nums):
    curr_max = nums[0]
    max_index = 0
    for i in range(len(nums)):
        if nums[i] > curr_max:
            curr_max = nums[i]
            max_index = i

    return max_index


def selection_sort(nums):
    start = 0
    end = len(nums) - 1
    while end > start:
        max_index = find_max(nums[:end + 1])
        temp = nums[max_index]
        nums[max_index] = nums[end]
        nums[end] = temp
        end -= 1
    return nums


print(selection_sort([4,1,2,7,5,4]))
