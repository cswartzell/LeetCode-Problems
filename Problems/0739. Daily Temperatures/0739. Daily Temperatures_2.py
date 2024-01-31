# 01-31-2024 Leetcode 739. Daily Temperatures
# https://leetcode.com/problems/daily-temperatures/?envType=daily-question&envId=2024-01-31
# Time: 5 Challenge: 3 of 10


# Monotonic decreasing stack of INDECIES, refer to the original arry to get their valuess

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        monostack = []
        ans = [0 for _ in range(len(temperatures))]
        idx = 0
        while idx < len(temperatures):
            while monostack != [] and temperatures[monostack[-1]] < temperatures[idx]:
                ans[monostack[-1]] = idx - monostack[-1]
                monostack.pop()
            monostack.append(idx)
            idx += 1

        return ans
            




