# 04-16-2023 Leetcode 1046. Last Stone Weight
# https://leetcode.com/problems/last-stone-weight/description/


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-1 * x for x in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            new_stone = heapq.heappop(stones) - heapq.heappop(stones)
            if new_stone != 0:
                heapq.heappush(stones, new_stone)
        return -1 * stones[0] if stones else 0
