# 04-23-2023 Leetcode 1372. Longest ZigZag Path in a Binary Tree
# https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def zig_zag(node, zigs, previous):
            if not node:
                return zigs
            if previous == "L":
                return max(
                    zig_zag(node.left, 0, "L"), zig_zag(node.right, zigs + 1, "R")
                )
            else:
                return max(
                    zig_zag(node.left, zigs + 1, "L"), zig_zag(node.right, 0, "R")
                )

        return zig_zag(root, -1, "L")
