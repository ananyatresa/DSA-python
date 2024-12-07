import math


class Solution:
    def is_safe(self, board, r, c, num):
        # check row n col
        for i in range(9):
            if board[i][c] == str(num) or board[r][i] == str(num):
                return False

        # check grid
        sqrt = int(math.sqrt(len(board)))
        r = r - r % sqrt
        c = c - c % sqrt
        for i in range(r, r + sqrt):
            for j in range(c, c + sqrt):
                if board[i][j] == str(num):
                    return False

        return True

    def sudoku(self, board, r, c):
        if r == len(board):
            return True

        if c == len(board[0]):
            return self.sudoku(board, r + 1, 0)

        # skip prefilled cells
        if board[r][c] != ".":
            return self.sudoku(board, r, c + 1)

        if board[r][c] == ".":
            for num in range(1, 10):
                if self.is_safe(board, r, c, num):
                    board[r][c] = str(num)
                    if self.sudoku(board, r, c + 1):
                        return True

                    # backtrack
                    board[r][c] = "."
            # trigger backtrack as no nums have satisfied conditions
            return False

    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.sudoku(board, 0, 0)

