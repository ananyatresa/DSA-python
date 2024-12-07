def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    arr_1 = merge_sort(arr[0: len(arr) // 2])
    arr_2 = merge_sort(arr[len(arr) // 2: len(arr)])

    i, j = 0, 0
    result = []
    while (i < len(arr_1)) and (j < len(arr_2)):
        if arr_1[i] < arr_2[j]:
            result.append(arr_1[i])
            i += 1
        else:
            result.append(arr_2[j])
            j += 1

    result.extend(arr_2[j:])
    result.extend(arr_1[i:])

    return result


print(merge_sort([4,-3,3,-3]))
