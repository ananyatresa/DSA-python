def word_maze(word, board):
    i = 0
    for r in range(len(board)):
        for c in range(len(board[0])):
            if word_search(word, board, r, c, i):
                return True

    return False


def word_search(word, board, r, c, i):
    if board[r][c] != word[i]:
        return False

    if i == len(word)-1:
        return True

    ch = board[r][c]

    #  marking as visited
    board[r][c] = "#"
    check = False

    # down
    if r < len(board) - 1:
        check = word_search(word, board, r + 1, c, i + 1)

    # right
    if c < len(board[0]) - 1 and check is False:
        check = word_search(word, board, r, c + 1, i + 1)

    # up
    if r > 0 and check is False:
        check = word_search(word, board, r - 1, c, i + 1)

    # left
    if c > 0 and check is False:
        check = word_search(word, board, r, c - 1, i + 1)

    board[r][c] = ch
    return check


board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCCED"
print(word_maze(word, board))
