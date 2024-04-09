# 04-08-2024 Leetcode 1155. Number of Dice Rolls With Target Sum
# https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/
# Time: 20 Challenge: 20


class Solution:
    def numRollsToTarget(self, n: int, k: int, t: int) -> int:
        dp = collections.defaultdict()
        dp[(0,t)] = 1

        def recurse(dice_remaining, curr_sum):
            if (dice_remaining, curr_sum) in dp:
                return dp[(dice_remaining, curr_sum)]
            
            elif dice_remaining == 0 or dice_remaining * k < t - curr_sum or dice_remaining > t - curr_sum:
                dp[(dice_remaining, curr_sum)] = 0

            else:
                dp[(dice_remaining, curr_sum)] = sum(recurse(dice_remaining - 1, curr_sum + roll) for roll in range(1, k + 1)) % (10**9 + 7)

            return dp[(dice_remaining, curr_sum)]

        return recurse(n, 0)