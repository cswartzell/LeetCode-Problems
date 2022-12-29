# 12-28-2022 1962. Remove Stones to Minimize the Total
# https://leetcode.com/problems/remove-stones-to-minimize-the-total/description/

import heapq


class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [-num for num in piles]
        heapq.heapify(heap)

        for _ in range(k):
            curr = -heapq.heappop(heap)
            remove = curr // 2
            heapq.heappush(heap, -(curr - remove))

        return -sum(heap)
