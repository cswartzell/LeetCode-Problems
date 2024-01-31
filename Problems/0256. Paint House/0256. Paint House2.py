# 01-29-2024 Leetcode Weekly 0256. Paint House
# https://leetcode.com/problems/paint-house/?envType=weekly-question&envId=2024-01-29
# Time: 15 mins Challenge: 5 of 10
# Classic DP problem, the only issue I had was being sure of the validity of the idea
# and which values to carry forward.

from functools import reduce


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        return min(reduce(lambda dp, h: [h[0] + min(dp[1], dp[2]), h[1] + min(dp[0], dp[2]), h[2] + min(dp[0], dp[1])], costs, [0,0,0]))


# class Solution:
#     def minCost(self, costs: List[List[int]]) -> int:
#         dp = costs[0]

#         for house in costs[1:]:
#             dp = [house[0] + min(dp[1], dp[2]), house[1] + min(dp[0], dp[2]), house[2] + min(dp[0], dp[1])]
#         return min(dp)


        # # options = {0:{1,2}, 1:{0,2}, 2:{0,1}}

        # # dp = [costs[0]]
        # dp = [0,0,0]

        # for house in costs:
        #     # dp.append([house[0] + min(dp[-1][1], dp[-1][2]), house[1] + min(dp[-1][0], dp[-1][2]), house[2] + min(dp[-1][0], dp[-1][1])])
        #     dp = [house[0] + min(dp[1], dp[2]), house[1] + min(dp[0], dp[2]), house[2] + min(dp[0], dp[1])]
        # # return min(dp[-1]
        # return min(dp)
