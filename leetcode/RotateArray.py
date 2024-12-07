def reverse( nums, start, end):
    while start <end:
        temp = nums[start]
        nums[start] = nums[end]
        nums[end] = temp
        start+=1
        end-=1


def rotate(nums, k):
    k = k % len(nums)
    if k < 0:
        k += len(nums)

    reverse(nums, 0, len(nums) - k-1)
    reverse(nums, len(nums) - k, len(nums)-1)
    reverse(nums, 0, len(nums)-1)
    print(nums)


nums=[-1,100,2,3]
rotate(nums, 2)