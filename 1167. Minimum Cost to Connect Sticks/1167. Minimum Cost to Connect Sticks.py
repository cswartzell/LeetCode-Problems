# 12-21-2022 Leetcode 1167. Minimum Cost to Connect Sticks
# https://leetcode.com/problems/minimum-cost-to-connect-sticks/description/

# is this honestly just sort n sum?
# No, I think you ALWAYS want to combine the
# two shortest sticks. This is a minheap problem
# two pops and a push
# boy was that easy

# Remember, python doesnt HAVE heaps. It has heap methods for lists


class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        total = 0

        heapq.heapify(sticks)

        while len(sticks) > 1:
            new_stick = heapq.heappop(sticks) + heapq.heappop(sticks)
            total += new_stick
            heapq.heappush(sticks, new_stick)

        return total
