# 09-11-2023 Neetcode 36. Valid Sudoku
# https://leetcode.com/problems/valid-sudoku/description/
# time: 15 mins

from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # have 9 sets for rows, 9 sets for cols, 9 sets for boxes.
        # rows and cols can just use rows and cols for indexing.
        # Need a forula that assigns (r,c) to a box:
        # box = (r//3 * 3) + (c//3)

        row = defaultdict(set)
        col = defaultdict(set)
        box = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                if board[r][c] in row[r]:
                    return False
                else:
                    row[r].add(board[r][c])
                
                if board[r][c] in col[c]:
                    return False
                else:
                    col[c].add(board[r][c])
                
                box_num = (r//3 * 3) + (c//3)
                if board[r][c] in box[box_num]:
                    return False
                else:
                    box[box_num].add(board[r][c])

        return True
