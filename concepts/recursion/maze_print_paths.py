def return_paths(p, r, c):
    if r == 1 and c == 1:
        return [p]

    arr=[]
    if r > 1:
        arr = return_paths(p + 'V', r - 1, c)
    if c > 1:
        arr.extend(return_paths(p + 'H', r, c - 1))

    return arr


row = 3
column = 3
print(return_paths("", row, column))




def print_paths(p, r, c):
    if r==1 and c==1:
        print(p)
        return

    if r>1:
        print_paths(p + 'V', r-1, c)
    if c>1:
        print_paths(p + 'H', r, c-1)



# row=3
# column=3
# print_paths("", row, column)