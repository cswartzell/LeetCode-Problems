# 12-09-2022 Leetcode 100. Same Tree
# https://leetcode.com/problems/same-tree/description/

# Convert each tree into a list. Compare lists

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def list_it(node):
            if not node:
                return ["X"]
            return [node.val] + list_it(node.left) + list_it(node.right)

        return list_it(p) == list_it(q)
