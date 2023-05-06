# 01-15-2023 Leetcode 2421. Number of Good Paths
# https://leetcode.com/problems/number-of-good-paths/

#Quite stupidly, the null path is a valid path. So at least n paths

#"only" 30,000 nodes, so O(n**2) is at least possible

class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int: