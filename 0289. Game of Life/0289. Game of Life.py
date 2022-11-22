"""04-20-2022 LeetCode 0289. Game of Life"""


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board) - 1
        cols = len(board[0]) - 1
        zero = 0

        for i in range(rows + 1):
            for j in range(cols + 1):
                board[i][j] += (
                    10 if i > zero and j > zero and board[i - 1][j - 1] % 10 > 0 else 0
                )
                board[i][j] += 10 if i > zero and board[i - 1][j - 0] % 10 > 0 else 0
                board[i][j] += (
                    10 if i > zero and j < cols and board[i - 1][j + 1] % 10 > 0 else 0
                )
                board[i][j] += 10 if j > zero and board[i - 0][j - 1] % 10 > 0 else 0
                board[i][j] += 10 if j < cols and board[i - 0][j + 1] % 10 > 0 else 0
                board[i][j] += (
                    10 if i < rows and j > zero and board[i + 1][j - 1] % 10 > 0 else 0
                )
                board[i][j] += 10 if i < rows and board[i + 1][j - 0] % 10 > 0 else 0
                board[i][j] += (
                    10 if i < rows and j < cols and board[i + 1][j + 1] % 10 > 0 else 0
                )

        for i in range(rows + 1):
            for j in range(cols + 1):
                if board[i][j] // 10 < 2 or board[i][j] // 10 > 3:  # rules 1 and 3
                    board[i][j] = 0
                if board[i][j] % 10 == 0 and board[i][j] // 10 == 3:  # rule 4
                    board[i][j] = 1
                board[i][j] %= 10  # clears summed data, rule 2 applied implicitly
