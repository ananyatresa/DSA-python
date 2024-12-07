def removeDuplicates(sort_list):
    j = 0  # keeps track of the current index
    for i in range(0, len(sort_list)):
        if j == 0 or j == 1 or sort_list[i] != sort_list[j - 2]:
            sort_list[j] = sort_list[i]
            j += 1
    return sort_list, j

sort_list = [1,2]
print(removeDuplicates(sort_list))

#1 2 2 3 3 3 4 5 5

