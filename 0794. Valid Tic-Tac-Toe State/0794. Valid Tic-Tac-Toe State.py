# 03-31-2023 Leetcode 794. Valid Tic-Tac-Toe State
# https://leetcode.com/problems/valid-tic-tac-toe-state/description/

#Ok, what are the fail states? num(x) >= num(o), and there cant be two
# winning rows on the same board or the game would have ended previously
# is that it? NO! Of course you can have multiple rows filled in all at once
# By placing a corner you can fill 2 rows in one go. Not three though, that would
# require 7 placements, which isnt possible. 

#So count the X wins and O wins. One must be zero, 

#Not sure what the least ugly version of this is. 

# OK! Its even more complicated. If X wins, it has to have placed one more mark than o
# If O wins, it needs to have exactly equal many marks as X (not less than)
# AND there can only be one winner. Otherwise, At most 1 more x than o

class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:

        #FINE. Ill write a generaic version. Few magic numbers, works for square boards of arbitrary size
        if len(board) != len(board[0]):
            raise Exception("Board not Square!")

        turn_count = {"X": 0, "O": 0, " ":0}
        for row in board:
            for c in row: 
                turn_count[c] += 1

        def horizontal(player) -> bool:
            return any(all(board[i][j] == player for j in range(len(board))) for i in range(len(board[0])))
        def vertical(player) -> bool:
            return any(all(board[i][j] == player for i in range(len(board))) for j in range(len(board[0])))
        def diagonal(player) -> bool:
            return any(all(board[i][i-j*(2*i+1)] == player for i in range(len(board))) for j in [0,1])
        
        X_wins = any([horizontal("X"), vertical("X"), diagonal("X")])
        O_wins = any([horizontal("O"), vertical("O"), diagonal("O")])

        if X_wins and O_wins:
            return False
        if X_wins:
            return turn_count["X"] - turn_count["O"] == 1
        if O_wins:
            return turn_count["X"] - turn_count["O"] == 0
        if turn_count["X"] - turn_count["O"] < 0 or turn_count["X"] - turn_count["O"] > 1:
            return False
        return True
