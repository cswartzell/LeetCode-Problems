# 03-31-2023 Leetcode 794. Valid Tic-Tac-Toe State
# https://leetcode.com/problems/valid-tic-tac-toe-state/description/

# Ok, what are the fail states? num(x) >= num(o), and there cant be two
# winning rows on the same board or the game would have ended previously
# is that it? NO! Of course you can have multiple rows filled in all at once
# By placing a corner you can fill 2 rows in one go. Not three though, that would
# require 7 placements, which isnt possible.

# So count the X wins and O wins. One must be zero,

# Not sure what the least ugly version of this is.

# OK! Its even more complicated. If X wins, it has to have placed one more mark than o
# If O wins, it needs to have exactly equal many marks as X (not less than)
# AND there can only be one winner. Otherwise, At most 1 more x than o


class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        turn_count = {"X": 0, "O": 0, " ": 0}
        for c in board[0] + board[1] + board[2]:
            turn_count[c] += 1

        X_wins = any(
            [
                board[0][0] == board[0][1] == board[0][2] == "X",
                board[1][0] == board[1][1] == board[1][2] == "X",
                board[2][0] == board[2][1] == board[2][2] == "X",
                board[0][0] == board[1][0] == board[2][0] == "X",
                board[0][1] == board[1][1] == board[2][1] == "X",
                board[0][2] == board[1][2] == board[2][2] == "X",
                board[0][0] == board[1][1] == board[2][2] == "X",
                board[0][2] == board[1][1] == board[2][0] == "X",
            ]
        )
        O_wins = any(
            [
                board[0][0] == board[0][1] == board[0][2] == "O",
                board[1][0] == board[1][1] == board[1][2] == "O",
                board[2][0] == board[2][1] == board[2][2] == "O",
                board[0][0] == board[1][0] == board[2][0] == "O",
                board[0][1] == board[1][1] == board[2][1] == "O",
                board[0][2] == board[1][2] == board[2][2] == "O",
                board[0][0] == board[1][1] == board[2][2] == "O",
                board[0][2] == board[1][1] == board[2][0] == "O",
            ]
        )

        if X_wins and O_wins:
            return False
        if X_wins:
            return turn_count["X"] - turn_count["O"] == 1
        if O_wins:
            return turn_count["X"] - turn_count["O"] == 0
        if (
            turn_count["X"] - turn_count["O"] < 0
            or turn_count["X"] - turn_count["O"] > 1
        ):
            return False
        return True
