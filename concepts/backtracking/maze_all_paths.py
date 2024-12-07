#  Backtracking introduction
def all_paths(p, maze, r, c):
    if r == len(maze) - 1 and c == len(maze[0]) - 1:
        return [p]

    #  Check if cell is visited or there is obstacle
    if not maze[r][c]:
        return []

    # mark the visited cell
    maze[r][c] = False

    arr = []
    # down
    if r < len(maze) - 1:
        arr = all_paths(p + "D", maze, r + 1, c)

    # right
    if c < len(maze[0]) - 1:
        arr.extend(all_paths(p + 'R', maze, r, c + 1))

    # up
    if r > 0:
        arr.extend(all_paths(p + 'U', maze, r - 1, c))

    # left
    if c > 0:
        arr.extend(all_paths(p + 'L', maze, r, c - 1))

    # revert the cell changes to its original so other paths can be explored
    maze[r][c] = True

    return arr


maze = [[True, True, True], [True, False, True], [False, True, True]]
print(all_paths("", maze, 0, 0))
