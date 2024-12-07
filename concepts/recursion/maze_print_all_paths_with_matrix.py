#  Backtracking introduction
def all_paths(p, maze, r, c, path, step):
    if r == len(maze) - 1 and c == len(maze[0]) - 1:
        print(p)
        path[r][c] = step
        for i in path:
            print(i)
        print("   ")
        return

    #  Check if cell is visited or there is obstacle
    if not maze[r][c]:
        return

    # mark current cell as visited for future recursion calls
    maze[r][c] = False

    path[r][c] = step

    # down
    if r < len(maze) - 1:
        all_paths(p + "D", maze, r + 1, c, path, step + 1)

    # right
    if c < len(maze[0]) - 1:
        all_paths(p + 'R', maze, r, c + 1, path, step + 1)

    # up
    if r > 0:
        all_paths(p + 'U', maze, r - 1, c, path, step + 1)

    # left
    if c > 0:
        all_paths(p + 'L', maze, r, c - 1, path, step + 1)

    # revert the cell changes to its original so other paths can be explored
    maze[r][c] = True
    path[r][c] = 0


maze = [[True, True, True], [True, True, True], [True, True, True]]
# path = [[0] * len(maze[0])] * len(maze)     #wont work because it creates references to the first list and not independent lists
path = [[0] * len(maze[i]) for i in range(len(maze))]
print(all_paths("", maze, 0, 0, path, 1))
