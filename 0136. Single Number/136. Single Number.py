"""02-15-2022 Leetcode https://leetcode.com/problems/single-number/ 136. Single Number"""

from collections import Counter


nums = [2, 2, 1]

c = Counter(nums)
print(x for x in nums if c[x] == 1)
