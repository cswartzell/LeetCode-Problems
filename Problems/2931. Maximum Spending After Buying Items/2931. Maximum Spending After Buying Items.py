# 04-01-2024 Leetcode 2931. Maximum Spending After Buying Items
# https://leetcode.com/problems/maximum-spending-after-buying-items/description/
# Time: 15 minutes Challenge: 4/10

class Solution:
    def maxSpending(self, values: List[List[int]]) -> int:
        # m, n = len(values), len(values[0])
        # heap = [(values[row][n-1], row, n-1) for row in range(m)]
        # heapq.heapify(heap)
        
        # total = 0

        # day = 1
        # while heap:
        #     item_val, item_row, item_col = heapq.heappop(heap)
        #     total += day * item_val
        #     if item_col > 0:
        #         heapq.heappush(heap, (values[item_row][item_col-1], item_row, item_col-1))
        #     day += 1

        # return total


        # return sum((day+1)*val for day, val in enumerate(sorted(chain.from_iterable(values))))
        return sum((day+1)*val for day, val in enumerate(sorted(sum(values, []))))