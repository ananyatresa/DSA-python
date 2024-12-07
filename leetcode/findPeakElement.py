def find_peak(arr):
    start=0
    end=len(arr)-1
    while start < end:
        mid = (start + end) // 2
        if arr[mid] > arr[mid+1]:
            end =mid
        else:
            start = mid+1
    return start

print(find_peak([4,5,6,7,0,1,2]))