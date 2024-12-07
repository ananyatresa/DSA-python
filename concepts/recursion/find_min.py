def find_min(arr, n):
    if n == 1:
        return arr[0]
    return min(arr[n-1], find_min(arr, n-1))


def main():
    arr=[1]
    print(find_min(arr, len(arr)))

main()