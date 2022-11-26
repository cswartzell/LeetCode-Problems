# 11-22-2022 LeetCoode 36. Valid Sudoku
# https://leetcode.com/problems/valid-sudoku/description/

# A very simple one, particularly as I had previously figured
# out the methods for obtaining the coordinates for squares in
# "boxes". There is actually a nicer way to iterate these using
# just a single counter, but its maybe less intuitive. If this was
# an interview I'd be satisfied with this. Using the hash is a
# straightforward choice, though I wanted to use Counter. Counter()
# does NOT inhereit Counter.values() though, so Id have had to iterate
# for [counter[x] in Counter.keys()], where I wanted max(Counter.values())


from collections import Counter


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            row_count, col_count, box_count = set(), set(), set()
            for col in range(9):
                if board[row][col] in row_count and board[row][col] != ".":
                    return False
                row_count.add(board[row][col])

                if board[col][row] in col_count and board[col][row] != ".":
                    return False
                col_count.add(board[col][row])

                if (
                    board[(col // 3) + (row // 3) * 3][(row % 3) * 3 + col % 3]
                    in box_count
                    and board[(col // 3) + (row // 3) * 3][(row % 3) * 3 + col % 3]
                    != "."
                ):
                    return False
                box_count.add(
                    board[(col // 3) + (row // 3) * 3][(row % 3) * 3 + col % 3]
                )
        return True
