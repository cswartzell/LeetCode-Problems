# 11-11-2022 LeetCode 37. Sudoku Solver
# https://leetcode.com/problems/sudoku-solver/description/

# Shall we attempt to use 9 digit binary to represent possibilities?
# A 1 being possible, 0 meaning not.

# Shall we assume we're being passed particularly simple sudoku puzzles
# as the input: ones where iteratively eliminating possibilities on a
# row, col, box basis is guarenteed to work? There are of course significantly
# more difficult classses of puzzles that require advanced techniques.
# Oh great... we are not only given basic puzzles

# Id say the next most advanced technique after basic elimination is pair-sets:
# If n squares share n posibilities within a grouping (row, col, box), then no
# other square within that grouping can contain any of the shared possibilites-
# they are bound to the n squares. Hopefully this technique isnt needed to solve
# this, as thats getting a bit out there. Still basic, but a bit of coding...

# After 90 minutes I've gotten it to work!!! For the first test case only...
# The logic is there and I THINK it is indeed running through and removing
# possibilities for every change made/squre solved. I guess the test cases include
# MORE than the most basic sudoku puzzles. Running the following test case:
# [[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]
# And printing a whacky mixed "solved squares and bin(possibilities)" I can see squares that have multiple possibilites
# BUT may be the only cell available for a given number for a row, col, or box.

# I guess I need to implement the NEXT level of logic. When we run out of changed squares,
# iterate through all remaining unsolved cells: for each row, col, box, IF the cell is the
# only possibility for a given number, change it to that number and add it to the changed stack

# STILL NOT ENOUGH! I guess we will have to implement the N sets of N possibilities per group
# elimination method, but frankly I'm tire of this problem and peeking at the solution it
# looks as if that may STILL not be enough. The given answer is "use backtracking", which baasically
# amounts to having the computer guess and check. Very frustrating that this is the listed solution.
# Its an lesson in trying to outhink the problem: I've wasted a number of hourse trying to
# algorithmically solve the problem as I would do it on paper. A computer can guess and check its
# way through, quickly so why bother with clever algos? Its really disappointing.


# Do not return anything, modify board in-place instead


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        # print original board for clarity:
        # for row in board:
        #     print(row)

        # Yes, these may unnecessary/clumsy, but I'm building as I go... We'll see what I use
        # Surely there is an elegant way to do this simply: 1<<ord(char-'a') or so. Less readable

        char_to_bin = {
            "1": 0b000000001,
            "2": 0b000000010,
            "3": 0b000000100,
            "4": 0b000001000,
            "5": 0b000010000,
            "6": 0b000100000,
            "7": 0b001000000,
            "8": 0b010000000,
            "9": 0b100000000,
            ".": 0b111111111,
        }
        bin_to_char = {
            0b000000001: "1",
            0b000000010: "2",
            0b000000100: "3",
            0b000001000: "4",
            0b000010000: "5",
            0b000100000: "6",
            0b001000000: "7",
            0b010000000: "8",
            0b100000000: "9",
            0b111111111: ".",
        }

        # setup binary board and preload set cells in changed stack for processing
        solved_cells = []
        bin_board = [[0 for _ in range(9)] for _ in range(9)]
        for row in range(9):
            for col in range(9):
                bin_board[row][col] = char_to_bin[board[row][col]]
                if board[row][col] != ".":
                    solved_cells.append((row, col, char_to_bin[board[row][col]]))

        # Remove 0b111111111 : '.' as a valid option in bin_to_char so we can use its
        # keys as "valid solved squares" dictionary instead of creating another
        bin_to_char.pop(0b111111111)

        while solved_cells:
            # print justified base 10 possibilities grid. Note cells with powers of two are solved:
            # for x in bin_board:
            #     print([str(y).rjust(3, " ") for y in x])
            # pass
            # print base 2 possibilities grid. Note cells with single '1' are solved:
            # print()
            # v
            # pass

            row, col, cell = solved_cells.pop()
            for i in range(9):
                # AND out ~cell with all in row
                if bin_board[row][i] not in bin_to_char:
                    bin_board[row][i] &= ~cell
                    # if cell solved, add to stack
                    if bin_board[row][i] in bin_to_char:
                        solved_cells.append((row, i, bin_board[row][i]))
                # AND out ~cell with all in col
                if bin_board[i][col] not in bin_to_char:
                    bin_board[i][col] &= ~cell
                    # if cell solved, add to stack
                    if bin_board[i][col] in bin_to_char:
                        solved_cells.append((i, col, bin_board[i][col]))
                # AND out ~cell with all in BOX
                # Clever boy trick to iterate through box cells using single offset counter
                box_row = (row // 3) * 3 + i // 3
                box_col = (col // 3) * 3 + i % 3
                if bin_board[box_row][box_col] not in bin_to_char:
                    bin_board[box_row][box_col] &= ~cell
                    # if cell solved, add to stack
                    if bin_board[box_row][box_col] in bin_to_char:
                        solved_cells.append(
                            (box_row, box_col, bin_board[box_row][box_col])
                        )

            # Did we run out of of changes? Solved? New Logic Level Time?
            if not solved_cells:
                unsolved = []
                for row in range(9):
                    for col in range(9):
                        if bin_board[row][col] not in bin_to_char:
                            unsolved.append((row, col, bin_board[row][col]))

                if not unsolved:
                    # Hey, we solved it
                    break

                # Well shoot. We have unsolved cells and base 'place and eliiminate' logic
                # has been exhausted. Time to check if remaining unsolved cells are the
                # only possibility for a given number in their row, col, or box.
                # Should we stop and go back a level of logic after finding a single new
                # set cell when using this logic? Or go through ALL unsolved cells at this
                # depth, solving them with this "level 2" logic and adding them to the
                # changed stack to be processed by another round of "level 1" logic later?

                while unsolved:
                    # DELETE THIS LINE: FORCED TEST FOR CELL WE KNOW CAN BE SOLVED
                    # unsolved = [(0,8,22)]

                    row, col, cell = unsolved.pop()
                    row_excluder = 0b111111111
                    col_excluder = 0b111111111
                    box_excluder = 0b111111111
                    for i in range(9):
                        # When & with cell, will leave only bits where 1 in unsolved cell, but 0 for all others
                        if i != col:
                            row_excluder &= ~bin_board[row][i]
                        # When & with cell, will leave only bits where 1 in unsolved cell, but 0 for all others
                        if i != row:
                            col_excluder &= ~bin_board[i][col]
                        # When & with cell, will leave only bits where 1 in unsolved cell, but 0 for all others
                        # Clever boy trick to iterate through box cells using single offset counter
                        box_row = (row // 3) * 3 + i // 3
                        box_col = (col // 3) * 3 + i % 3
                        pass
                        if not (box_row == row and box_col == col):
                            box_excluder &= ~bin_board[box_row][box_col]

                    # & "anti-excluvises" with cell, leaving a single bit on if unsolved cell must be a given
                    # digit, being the only cell in that row, col, box with the possibility of doing so
                    row_sinlge = row_excluder & cell
                    col_sinlge = col_excluder & cell
                    box_sinlge = box_excluder & cell

                    # if cell solved, add to stack
                    if row_sinlge in bin_to_char:
                        bin_board[row][col] = row_sinlge
                        solved_cells.append((row, col, row_sinlge))
                    elif col_sinlge in bin_to_char:
                        bin_board[row][col] = col_sinlge
                        solved_cells.append((row, col, col_sinlge))
                    elif box_sinlge in bin_to_char:
                        bin_board[row][col] = box_sinlge
                        solved_cells.append((row, col, box_sinlge))

                    # print()
                    # for x in bin_board:
                    #     print([str(bin(y))[2:].rjust(9, "0") for y in x])
                    # pass

        # Convert binary board to char board INCLUDING whacky mixed results of solved squares as base 10 and unsolved 9 binary digit base 2 strings
        # for row in range(9):
        #     for col in range(9):
        #         board[row][col] = str(bin_to_char[bin_board[row][col]]).rjust(9, " ") if bin_board[row][col] in bin_to_char else str(bin(bin_board[row][col]))[2:].rjust(9, "0")
        # pass

        # #Convert binary board to char board when it works and its actually solved...
        for row in range(9):
            for col in range(9):
                board[row][col] = bin_to_char[bin_board[row][col]]
        pass

        # Print solved result
        print()
        for row in board:
            print(row)
        pass
        return

        # NO RETURN. Yes... this isnt modify in place, this is creating a whole parallel board and then translating it to the
        # original. I dont want to work with char board as it seems cumbersome. May try it next. Binary version seemed more interesting
        # It DOESNT say we cant use extra memory.
