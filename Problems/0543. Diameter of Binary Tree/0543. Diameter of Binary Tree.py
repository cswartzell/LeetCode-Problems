# 02-26-2024 Leetcode 543. Diameter of Binary Tree
# https://leetcode.com/problems/diameter-of-binary-tree/?envType=daily-question&envId=2024-02-27
# Time: 10 mins Challenge 2/10


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diam = 0
        def dfs(root):
            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)
            self.diam = max(self.diam, left + right)

            return max(left, right) + 1

        dfs(root)
        return self.diam
