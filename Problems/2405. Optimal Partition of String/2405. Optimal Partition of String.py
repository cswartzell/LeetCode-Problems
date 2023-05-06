# 04-03-2023 Leetcode 2405. Optimal Partition of String
# https://leetcode.com/problems/optimal-partition-of-string/description/


# linear scan, frequency map. Or just set. When you find a letter in the set
# just empty it, increment the substring count and continue. Easiest medium ever


class Solution:
    def partitionString(self, s: str) -> int:
        seen = set()
        ans = 1
        for letter in s:
            if letter in seen:
                ans += 1
                seen = {letter}
            else:
                seen.add(letter)
        return ans
