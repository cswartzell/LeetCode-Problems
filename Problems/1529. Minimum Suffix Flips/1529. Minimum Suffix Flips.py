# 04-03-2023 Leetcode 1529. Minimum Suffix Flips
# https://leetcode.com/problems/minimum-suffix-flips/description/

# I think this is just the number of "01" or "10"s in the string from right to left.
# Append a leading zero to start, then just linear scan two chars at a time.


class Solution:
    def minFlips(self, target: str) -> int:
        ans = 0
        target = "0" + target
        for i in range(1, len(target)):
            if target[i] != target[i - 1]:
                ans += 1
            # ans += 1 if target[i] != target[i-1] else 0
        return ans

        # target = "0" + target
        # # flip = {"10", "01"}
        # ans = 0
        # for i in range(len(target) - 1):
        #     if target[i:i+2] in flip:
        #         ans += 1
        # return ans
