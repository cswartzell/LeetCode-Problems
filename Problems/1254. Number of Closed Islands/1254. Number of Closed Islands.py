# 04-06-2023 1254. Number of Closed Islands
# https://leetcode.com/problems/number-of-closed-islands/description/


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        # just for fun/future prep, lets label the flood filled islands
        land_name = 0
        ans = 0

        for row_i in range(len(grid)):
            for col_i in range(len(grid[0])):
                if grid[row_i][col_i] == 0:
                    land_name -= 1
                    land_ho = [(row_i, col_i)]
                    isolated = True
                    while land_ho:
                        curr_row_i, curr_col_i = land_ho.pop()
                        grid[curr_row_i][curr_col_i] = land_name
                        if (
                            curr_row_i == 0
                            or curr_row_i == len(grid) - 1
                            or curr_col_i == 0
                            or curr_col_i == (len(grid[0])) - 1
                        ):
                            isolated = False
                        for row_offset, col_offset in (
                            (-1, 0),
                            (1, 0),
                            (0, -1),
                            (0, 1),
                        ):
                            if (
                                curr_row_i + row_offset < 0
                                or curr_row_i + row_offset == len(grid)
                                or curr_col_i + col_offset < 0
                                or curr_col_i + col_offset == (len(grid[0]))
                            ):
                                continue
                            elif (
                                grid[curr_row_i + row_offset][curr_col_i + col_offset]
                                == 0
                            ):
                                land_ho.append(
                                    (curr_row_i + row_offset, curr_col_i + col_offset)
                                )
                    if isolated == True:
                        ans += 1
        return ans

        # Step 1: flood fill from edges to remove "land masses that extend off map"
        # We CAN just make these water and it wont affect existing islands, for if it did
        # they would be ATTACHED to said landmass and be swept away as well.
        # All remainging land is island land. Then union find to seperate islands

        # I stopped the following realizing its overly complex. May be a good solution
        # depending on density of islands. Instead just flood fill/union ALL land, and
        # keep a table of union root if you discover continental

        # continental = set()
        # for i in range(len(grid[0])):
        #     if grid[0][i] == 0:
        #         continental.add((0, i))
        # for i in range(len(grid[0])):
        #     if grid[len(grid) - 1][i] == 0:
        #         continental.add((len(grid) - 1, i))
        # for i in range(len(grid)):
        #     if grid[i][0] == 0:
        #         continental.add((i, 0))
        # for i in range(len(grid)):
        #     if grid[i][len(grid[0])-1] == 0:
        #         continental.add((i, 0))

        # while continental:
        #     x, y = continental.pop()
        #     grid
