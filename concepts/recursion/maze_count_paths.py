def count_paths(r, c):
    if r==1 or c==1:
        return 1

    down = count_paths(r-1, c)
    right = count_paths(r, c-1)

    return down + right


row=3
column=3
print(count_paths(row, column))