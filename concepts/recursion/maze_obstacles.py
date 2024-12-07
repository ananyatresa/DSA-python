def paths_w_obstacles(p,maze,r,c):
    if r == len(maze)-1 and c == len(maze[0])-1:
        return [p]

    # checking obstacle at each cell
    if maze[r][c]:
        return []

    arr = []
    # down
    if r < len(maze)-1:
        arr = paths_w_obstacles(p + 'D', maze, r+1, c)

    # diagonal
    if r < len(maze)-1 and c < len(maze[0])-1:
        arr.extend(paths_w_obstacles(p + 'G', maze, r+1, c + 1))

    # right
    if c < len(maze[0])-1:
        arr.extend(paths_w_obstacles(p + 'R', maze, r, c+1))

    return arr


maze = [[False, False, False], [False, True, False], [False, False, False]]
print(paths_w_obstacles('', maze, 0, 0))