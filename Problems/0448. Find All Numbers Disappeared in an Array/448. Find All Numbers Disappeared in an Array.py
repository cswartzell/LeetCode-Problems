"""02-15-2022 Leetcode Find All Numbers Disappeared in an Array"""
from collections import Counter

nums = [4, 3, 2, 7, 8, 2, 3, 1]
print(list(x for x in range(1, len(nums)) if x not in Counter(nums)))
# aww yiss sweet, and clear, one liner
