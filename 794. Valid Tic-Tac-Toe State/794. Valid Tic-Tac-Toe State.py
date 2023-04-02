
class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        turn_count = {"X": 0, "O": 0, " ":0}
        for c in board[0] + board[1] + board[2]:
            turn_count[c] += 1

        def horizontal(player) -> bool:
            return any(all(board[i][j] == player for j in range(len(board)) for i in range(len(board[0]))))
        def vertical(player) -> bool:
            return any(all(board[i][j] == player for i in range(len(board)) for j in range(len(board[0]))))
        def diagonal(player) -> bool:
            return any(all(board[i][i-j*(2*i+1)] == player for i in range(len(board)) for j in [0,1]))

        X_wins = any(horizontal("X"), vertical("X"), diagonal("X"))
        O_wins = any(horizontal("O"), vertical("O"), diagonal("O"))

        if X_wins and O_wins:
            return False
        if X_wins:
            return turn_count["X"] - turn_count["O"] == 1
        if O_wins:
            return turn_count["X"] - turn_count["O"] == 0
        if turn_count["X"] - turn_count["O"] < 0 or turn_count["X"] - turn_count["O"] > 1:
            return False
        return True
