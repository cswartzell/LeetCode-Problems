# 04-20-2023 Leetcode 437. Path Sum III
# https://leetcode.com/problems/path-sum-iii/description/
# DFS and Count

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def DFS(node, curr_sums):
            if not node:
                return 0
            found = 1 if node.val == targetSum else 0
            for idx in range(len(curr_sums)):
                curr_sums[idx] += node.val
                if curr_sums[idx] == targetSum:
                    found += 1
            curr_sums += [node.val]
            return DFS(node.left, curr_sums[:]) + DFS(node.right, curr_sums[:]) + found

        return DFS(root, [])
