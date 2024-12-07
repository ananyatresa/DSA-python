def search(nums, target):
    start=0
    end=len(nums)-1
    while start<=end:
        mid = int(start + (end-start)/2)
        if target>nums[mid]:
            start=mid+1
        elif target<nums[mid]:
            end=mid-1
        else:
            return mid
    return -1

nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 18, 20, 25, 28, 34, 39, 45, 47, 51]
target = 47
print(search(nums, target))