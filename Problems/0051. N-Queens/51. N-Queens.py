"""06-04-2022 Leetcode 51. N-Queens"""
# Ok, so I was actually very much on the right track: Keep track
# of states and place a single queen at a time, store the grid
# if we fill it, backtrack if we cannot. I tried using a list of
# possible remaining positions (as tuples), but as I suspected
# this involved far too much iterating. We should be able to knock
# out an entire row, col, diagonal (and "anti-diagonal") in one go:
# and we can. It should have been obvious- rather than creating a list
# of all possibilities and whitling that down, we can instead keep a
# set of all OCCUPIED rows, cols, diags, adiags and only allow adding
# a queen if not already in any of those sets.


class Solution:
    def __init__(self) -> None:
        self.full_grids = []
        self.n = 0

    def solveNQueens(self, n: int):  # -> List[List[str]]:
        self.n = n
        rows, cols, dygs, adgs, curq = [], [], [], [], []
        placed = 0

        for x in range(0, n):
            for y in range(0, n):
                self.placeQueen(rows, cols, dygs, adgs, x, y, placed, curq)

        self.format_grids
        return self.full_grids

    def placeQueen(self, rows, cols, dygs, adgs, x, y, placed, curq):
        if x not in rows and y not in cols and x + y not in adgs and x - y not in dygs:
            placed += 1
            if placed == self.n:
                self.full_grids.append([curq])
                return

            rows.append(x)
            cols.append(y)
            dygs.append(x - y)
            adgs.append(x + y)
            curq.append((x, y))

            # y += 1
            # if y == self.n-1:
            #     if x < self.n:
            #         y = -1
            #         x += 1
            #     else: return
            for new_x in range(x, self.n):
                for new_y in range(y, self.n):
                    self.placeQueen(rows, cols, dygs, adgs, new_x, new_y, placed, curq)
        return

    def format_grids(self):
        pass


tested = Solution()
print(tested.solveNQueens(5))

# # 1:1, 2:2, 3:0?, 4:2, 5:? I found one arangement that has no symetry, so 8? AND has a corner used
# # Ok, so n is only up til 9, relatively small. Obviously combinations on
# # a 9X9 board are fucking huge, but it narrows stupid quick too.
# # Every placed queen eliminates a MASSIVE chunk of possibilities.
# # The starting choice though is 81 possibilites, and placing a queen
# # eliminates somewhere beteween 32 and 17 choices. Is simulating this with
# # random choice possible? I mean... I could put the coordinates in a stack, then
# # recursively call all possibilities in the stack. Its only 9 calls deep at worst
# # and most terminate very early. The widest call is 81 in round 1, but it narrows soo
# # stupid fast maybe its fine. Brute Force Baby. Try in VSC first and check timing.

# # Strongly suspect its in powers of two depending on what sort of symetries in solution

# import itertools


# class Solution:
#     def solveNQueens(self, n: int):  # -> List[List[str]]:
#         grid = [["0" for _ in range(n)] for _ in range(n)]
#         stck = set(itertools.product(range(n), range(n)))
#         placed_queens = 0
#         self.recurseQueens(grid, stck, placed_queens)
#         return grid

#     def recurseQueens(self, grid, stck, placed_queens):
#         if not stck and placed_queens < len(grid):
#             return 0, 0, 0  # no space for remaining queens

#         for pos in stck:
#             new_grid, new_stack, new_placed_queens = self.placeQueen(
#                 grid, stck, pos, placed_queens
#             )
#             if new_placed_queens == 0:
#                 stck.discard(pos)
#                 return
#             if new_placed_queens == len(grid):
#                 print(new_grid)  # just turn this into a return?
#                 return
#             self.recurseQueens(new_grid, new_stack, new_placed_queens)

#     def placeQueen(self, grid, stck, pos, placed_queens):
#         pos_x, pos_y = pos[1], pos[0]  # why not *pos ?
#         n = len(grid)
#         for x in range(n):
#             grid[pos_y][x] = "."
#             stck.discard((pos_y, x))
#         for y in range(n):
#             grid[y][pos_x] = "."
#             stck.discard((y, pos_x))
#         for diag in range(1, n):
#             if pos_x + diag < n and pos_y + diag < n:
#                 grid[pos_y + diag][pos_x + diag] = "."
#                 stck.discard((pos_y + diag, pos_x + diag))
#             if pos_x + diag < n and pos_y - diag >= 0:
#                 grid[pos_y - diag][pos_x + diag] = "."
#                 stck.discard((pos_y - diag, pos_x + diag))
#             if pos_x - diag >= 0 and pos_y + diag < n:
#                 grid[pos_y + diag][pos_x - diag] = "."
#                 stck.discard((pos_y + diag, pos_x - diag))
#             if pos_x - diag >= 0 and pos_y - diag >= 0:
#                 grid[pos_y - diag][pos_x - diag] = "."
#                 stck.discard((pos_y - diag, pos_x - diag))

#         grid[pos_y][pos_x] = "Q"
#         return grid, stck, placed_queens + 1


# tested = Solution()
# print(tested.solveNQueens(3))


# # import itertools


# # class Solution:
# #     def solveNQueens(self, n: int):  # -> List[List[str]]:
# #         grid = [["0" for _ in range(n)] for _ in range(n)]
# #         stck = set(itertools.product(range(n), range(n)))
# #         placed_queens = 0
# #         self.recurseQueens(grid, stck, placed_queens)
# #         return grid

# #     def recurseQueens(self, grid, stck, placed_queens):
# #         if not stck and placed_queens < len(grid):
# #             return _, _, 0  # no space for remaining queens

# #         for pos in stck:
# #             grid, stck = self.placeQueen(grid, stck, pos)


# #     def placeQueen(self, grid, stck, pos):
# #         pos_x, pos_y = pos[1], pos[0]  # why not *pos ?
# #         n = len(grid)
# #         for x in range(n):
# #             grid[pos_y][x] = "."
# #             stck.discard((pos_y, x))
# #         for y in range(n):
# #             grid[y][pos_x] = "."
# #             stck.discard((y, pos_x))
# #         for diag in range(1, n):
# #             if pos_x + diag < n and pos_y + diag < n:
# #                 grid[pos_y + diag][pos_x + diag] = "."
# #                 stck.discard((pos_x + diag, pos_y + diag))
# #             if pos_x + diag < n and pos_y - diag >= 0:
# #                 grid[pos_y - diag][pos_x + diag] = "."
# #                 stck.discard((pos_x + diag, pos_y - diag))
# #             if pos_x - diag >= 0 and pos_y + diag < n:
# #                 grid[pos_y + diag][pos_x - diag] = "."
# #                 stck.discard((pos_x - diag, pos_y + diag))
# #             if pos_x - diag >= 0 and pos_y - diag >= 0:
# #                 grid[pos_y - diag][pos_x - diag] = "."
# #                 stck.discard((pos_x - diag, pos_y - diag))

# #         grid[pos_y][pos_x] = "Q"
# #         return grid, stck


# # tested = Solution()
# # print(tested.solveNQueens(5))
