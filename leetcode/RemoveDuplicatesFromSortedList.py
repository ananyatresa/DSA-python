#2 pointer method: 1 for current index of unique elements and 2nd for iterating the list to check
# with previous element

def remove_duplicates(sort_list):
    j = 0  # keeps track of the current index
    for i in range(0, len(sort_list)):
        if j == 0 or sort_list[i] != sort_list[i - 1]:
            sort_list[j] = sort_list[i]
            j += 1
    return sort_list, j


# sort_list = [1, 2, 2, 3, 4, 5, 5, 5, 5, 6, 7]
sort_list = [1,1,2,2,3,4,5]
print(remove_duplicates(sort_list))
