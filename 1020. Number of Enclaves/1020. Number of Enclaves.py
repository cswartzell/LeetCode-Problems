# 04-07-2023 Leetcode 1020. Number of Enclaves
# https://leetcode.com/problems/number-of-enclaves/description/


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        # just for fun/future prep, lets label the flood filled islands
        # BFS EDGES ONLY
        def BFS(row_i, col_i):
            land_queue = [(row_i, col_i)]
            while land_queue:
                curr_row, curr_col = land_queue.pop()
                grid[curr_row][curr_col] = 0
                for row_offset, col_offset in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    new_row, new_col = curr_row + row_offset, curr_col + col_offset
                    if (
                        new_row == -1
                        or new_row == len(grid)
                        or new_col == -1
                        or new_col == len(grid[0])
                    ):  # SHOULDNT need >= len, can just bail AT len (or -1 for that matter)
                        continue
                    if grid[new_row][new_col] == 1:
                        land_queue.append((new_row, new_col))

        # TOP:
        for i in range(len(grid[0])):
            if grid[0][i] == 1:
                BFS(0, i)
        # BOTTOM:
        for i in range(len(grid[0])):
            if grid[len(grid) - 1][i] == 1:
                BFS(len(grid) - 1, i)
        # LEFT:
        for i in range(len(grid)):
            if grid[i][0] == 1:
                BFS(i, 0)
        # RIGHT:
        for i in range(len(grid)):
            if grid[i][len(grid[0]) - 1] == 1:
                BFS(i, len(grid[0]) - 1)

        ans = 0
        for i in range(1, len(grid) - 1):
            for j in range(1, len(grid[0]) - 1):
                if grid[i][j] == 1:
                    ans += 1
        return ans
        # return sum(sum(grid,[])) #Bad practice but I like it

        # ans = 0

        # for row_i in range(len(grid)):
        #     for col_i in range(len(grid[0])):
        #         if grid[row_i][col_i] == 1:
        #             land_ho = [(row_i, col_i)]
        #             count = 1
        #             isolated = True
        #             while land_ho:
        #                 curr_row_i, curr_col_i = land_ho.pop()
        #                 grid[curr_row_i][curr_col_i] = 0
        #                 if curr_row_i == 0 or curr_row_i == len(grid) - 1 or curr_col_i == 0 or curr_col_i == (len(grid[0])) - 1:
        #                     isolated = False
        #                 for row_offset, col_offset in ((-1,0),(1,0),(0,-1),(0,1)):
        #                     if curr_row_i + row_offset < 0 or curr_row_i + row_offset == len(grid) or curr_col_i + col_offset < 0 or curr_col_i + col_offset == (len(grid[0])):
        #                         continue
        #                     elif grid[curr_row_i + row_offset][curr_col_i + col_offset] == 1:
        #                         count += 1
        #                         land_ho.append((curr_row_i + row_offset, curr_col_i + col_offset))
        #             if isolated == True:
        #                 ans += count
        # return ans
