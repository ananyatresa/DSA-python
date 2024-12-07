## 3 pointer method: 1 for largest elem in 1st list, 2nd for largest elem in 2nd list
# and 3rd for last index pos in 1s list. Then decerement respective i/j and k pointers based
# on which has larger elem

def merge(nums1, nums2, m, n):
    i = m - 1
    j = n - 1
    k = len(nums1) - 1

    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            k -= 1
            i -= 1
        else:
            nums1[k] = nums2[j]
            k -= 1
            j -= 1
    return nums1


nums1 = [1, 2, 3, 5, 0, 0, 0]
nums2 = [2, 7, 8]
m = 4
n = 3
print(merge(nums1, nums2, m, n))

# [1 2 2 3 5 7 8]
