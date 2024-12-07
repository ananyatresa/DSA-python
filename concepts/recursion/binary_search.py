def search(arr, target, start, end):
    if start >= end:
        return start

    mid = (start + end) // 2
    if target > arr[mid]:
        return search(arr, target, mid + 1, end)
    elif target < arr[mid]:
        return search(arr, target, start, mid - 1)
    else:
        return mid


arr = [1, 2, 2, 2, 5, 6]
print(search(arr, 2, 0, len(arr) - 1))
