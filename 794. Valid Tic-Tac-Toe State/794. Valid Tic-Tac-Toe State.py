class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:

        sum(
            board[0][0] == board[0][1] == board[0][2] == "X",
            board[1][0] == board[1][1] == board[1][2] == "X",
            board[2][0] == board[2][1] == board[2][2] == "X",
            board[0][0] == board[0][1] == board[0][2] == "O",
            board[1][0] == board[1][1] == board[1][2] == "O",
            board[2][0] == board[2][1] == board[2][2] == "O",
            board[0][0] == board[1][0] == board[2][0] == "X",
            board[0][1] == board[1][1] == board[2][1] == "X",
            board[0][2] == board[1][2] == board[2][2] == "X",
            board[0][0] == board[1][0] == board[2][0] == "O",
            board[0][1] == board[1][1] == board[2][1] == "O",
            board[0][2] == board[1][2] == board[2][2] == "O",
            board[0][0] == board[1][1] == board[2][2] == "X",
            board[0][2] == board[1][1] == board[2][0] == "X",
            board[0][0] == board[1][1] == board[2][2] == "O",
            board[0][2] == board[1][1] == board[2][0] == "O",
        )
