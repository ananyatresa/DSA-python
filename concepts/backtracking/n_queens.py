def valid_board(board):
    result = []
    for row in board:
        s = ''
        for elem in row:
            if elem:
                s += 'Q'
            else:
                s += '.'
        result.append(s)
    return [result]


def display(board):
    for row in board:
        for elem in row:
            if elem:
                print('Q ', end="")
            else:
                print('. ', end="")
        print("")


def is_safe(board, r, c):

    # Above
    for i in range(r+1):
        if board[i][c]:
            return False

    # Upper left diagonal
    max_left = min(r, c)        # Max possible left range to check the diagonal cells
    for i in range(max_left+1):
        if board[r-i][c-i]:
            return False

    # Upper left diagonal
    max_right = min(r, len(board) - c - 1)    # Max possible right range to check the diagonal cells
    for i in range(max_right+1):
        if board[r - i][c + i]:
            return False

    return True


def solve_n_queens(board, r):
    # base condition
    if r == len(board):
        # found 1 possible answer as we have placed a queen in last row and come out of bounds(r=n+1 here)
        # display(board)
        # print()
        return valid_board(board)

    result_list=[]

    for c in range(len(board)):
        if is_safe(board, r, c):
            board[r][c] = True                          # placed queen
            result_list.extend(solve_n_queens(board, r+1))      # calling next row queen placement
            board[r][c] = False                         # backtrack

    return result_list


n=4
board = [[False] * n for _ in range(n)]
# print(board)
print(solve_n_queens(board, 0))



