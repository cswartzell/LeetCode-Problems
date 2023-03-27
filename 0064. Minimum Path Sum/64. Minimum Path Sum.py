# 03-2-26-2023 Leetcode 64. Minimum Path Sum
# https://leetcode.com/problems/minimum-path-sum/description/

# Queue based BFS flood fill? Have to process whole queue
# Max grid is 200x200 with score 100, so max score is 4_000_000
# (or actually 100 less?)

import collections


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        grid_q = collections.deque()
        # (row_idx, col_idx, current_cost)
        grid_q.append((0, 0, grid[0][0]))
        max_row, max_col = len(grid), len(grid[0])
        sum_grid = [[4_000_001 for _ in range(max_col)] for _ in range(max_row)]
        sum_grid[0][0] = grid[0][0]

        while grid_q:
            row, col, curr_score = grid_q.popleft()
            # We are adding to the queue AND updating sum_grid as we go. If we find
            # a node in the queue that has been superceded by another route to the same
            # cell in less time, dont bother processing it again.
            if sum_grid[row][col] < curr_score:
                continue
            for x_offset, y_offset in ((1, 0), (0, 1)):
                curr_row = row + x_offset
                curr_col = col + y_offset
                if curr_row < max_row and curr_col < max_col:
                    if (
                        grid[curr_row][curr_col] + curr_score
                        < sum_grid[curr_row][curr_col]
                    ):
                        sum_grid[curr_row][curr_col] = (
                            grid[curr_row][curr_col] + curr_score
                        )
                        grid_q.append(
                            (curr_row, curr_col, sum_grid[curr_row][curr_col])
                        )

        return sum_grid[max_row - 1][max_col - 1]
