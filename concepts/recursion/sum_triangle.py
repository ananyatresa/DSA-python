
def triangle(arr):
    if len(arr) == 1:
        return
    new_arr = []
    for i in range(len(arr)-1):
        new_arr.append(arr[i] + arr[i+1])

    triangle(new_arr)
    print(new_arr)



def main():
    arr = [1,2,3,4,5]
    triangle(arr)
    print(arr)

main()