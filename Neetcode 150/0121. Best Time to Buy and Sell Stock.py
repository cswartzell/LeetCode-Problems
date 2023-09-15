# 11-14-2023 Neetcode 121. Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Time: 5 mins

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        lowest = prices[0]

        for i in range(1, len(prices)):
            lowest = min(lowest, prices[i])
            max_profit = max(max_profit, prices[i] - lowest)

        return max_profit


# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         low, high = prices[-1], prices[-1]
#         profit = 0

#         for i in range(len(prices) - 2, -1, -1):
#             if prices[i] < low:
#                 low =  prices[i]
#                 profit = max(profit, high - low)
#             elif prices[i] > high:
#                 low, high = prices[i], prices[i]
#         return profit