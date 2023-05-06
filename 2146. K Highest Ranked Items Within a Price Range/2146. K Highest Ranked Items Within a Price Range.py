# 04-23-2023 Leetcide 2146. K Highest Ranked Items Within a Price Range
# https://leetcode.com/problems/k-highest-ranked-items-within-a-price-range/description/

# Collect first k items that meet the following criteria
# Rules, in order:
# 1) Distance (manhattan?) (low is better)
# 2) Price (low is better)
# 3) Row Number (low is better)
# 4) Col Number (low is better)

# Python sorts tuples by first element, then second, then third...
# so we can just save items that match our criteria into a list.
# Furthermore, sort is low->high which is how we want our criteria sorted in every category anyhow
# ONCE we hit k+items, we FINISH searching the current distance, and continue to add items.
# Then we merely sort, and return the first k items
# OR we could push them into a heap in the first place, and just pop off k items.
# Lets try both and speed compare!

# DO note we may not find k items. Need to keep track of seen while BFSing of course
import heapq


class Solution:
    def highestRankedKItems(
        self, grid: List[List[int]], pricing: List[int], start: List[int], k: int
    ) -> List[List[int]]:
        items = []
        queue = collections.deque([(start[0], start[1])])

        seen = set([(start[0], start[1])])
        dist = -1
        while queue and len(items) < k:
            dist += 1
            for _ in range(len(queue)):
                curr_row, curr_col = queue.popleft()
                if (
                    grid[curr_row][curr_col] >= pricing[0]
                    and grid[curr_row][curr_col] <= pricing[1]
                ):
                    heapq.heappush(
                        items, (dist, grid[curr_row][curr_col], curr_row, curr_col)
                    )
                for row_offset, col_offset in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    new_row, new_col = curr_row + row_offset, curr_col + col_offset
                    if (
                        new_row >= 0
                        and new_row < len(grid)
                        and new_col >= 0
                        and new_col < len(grid[0])
                    ):
                        if (new_row, new_col) not in seen and grid[curr_row][
                            curr_col
                        ] != 0:
                            seen.add((new_row, new_col))
                            queue.append((new_row, new_col))

        return [
            [row, col] for _, _, row, col in heapq.nsmallest(min(k, len(items)), items)
        ]

        # items = []
        # queue = collections.deque([(start[0], start[1])])

        # seen = set([(start[0], start[1])])
        # dist = -1
        # while queue and len(items) < k:
        #     dist += 1
        #     for _ in range(len(queue)):
        #         curr_row, curr_col = queue.popleft()
        #         if grid[curr_row][curr_col] >= pricing[0] and grid[curr_row][curr_col] <= pricing[1]:
        #             items.append( (dist, grid[curr_row][curr_col], curr_row, curr_col) )
        #         for row_offset, col_offset in ((-1,0), (1,0), (0,-1), (0,1)):
        #             new_row, new_col = curr_row + row_offset, curr_col + col_offset
        #             if new_row >= 0 and new_row < len(grid) and new_col >= 0 and new_col < len(grid[0]):
        #                 if (new_row, new_col) not in seen and grid[curr_row][curr_col] != 0:
        #                     seen.add((new_row, new_col))
        #                     queue.append((new_row, new_col))

        # return [[row, col] for _, _, row, col in sorted(items)[:min(k, len(items))]]
