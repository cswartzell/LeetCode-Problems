# 03-31-2023 Leetcode 1394. Find Lucky Integer in an Array
# https://leetcode.com/problems/find-lucky-integer-in-an-array/description/


import functools


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        l_c = collections.Counter(arr)
        return max(x if x == l_c[x] else -1 for x in l_c.keys())

        # return max(x if x == (l_c := collections.Counter(arr))[x] else -1 for x in l_c.keys())

        #         (l_c := collections.Counter(arr)).update({-1:-1})
        # return max(x for x in l_c if x == l_c[x])
