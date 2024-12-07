def sort(arr, m, n, swapped):
    if m == len(arr):
        return arr
    if n == len(arr) - m:
        if not swapped:
            return arr
        return sort(arr, m+1, 1, False)
    if arr[n] < arr[n-1]:
        temp = arr[n]
        arr[n] = arr[n-1]
        arr[n-1] = temp
        swapped = True
    return sort(arr, m, n+1, swapped)

print(sort([2,2,1,1,4,4,3,6,1,4,5] , 0, 1, False))
