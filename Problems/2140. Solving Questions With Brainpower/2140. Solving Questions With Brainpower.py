# 04-08-2023 Leetcode 2140. Solving Questions With Brainpower
# https://leetcode.com/problems/solving-questions-with-brainpower/description/
#10**5 question len is rather a lot, so I dont know that 

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp = [0]*(len(questions) + 1)
        max_seen = 0
        for i in range(len(questions) -1, -1, -1):
            dp[i] = max(questions[i][0] + dp[min(i + questions[i][1] + 1, len(dp) - 1)], max_seen)
            max_seen = max(max_seen, dp[i])
        return max_seen