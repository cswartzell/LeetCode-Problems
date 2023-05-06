# 01-07-2023 Leetcode 1833. Maximum Ice Cream Bars
# https://leetcode.com/problems/maximum-ice-cream-bars/


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        bars = 0
        for i in range(len(costs)):
            coins -= costs[i]
            if coins >= 0:
                bars += 1
            else:
                break
        return bars
