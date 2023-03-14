# 03-13-2023 Leetcode 129. Sum Root to Leaf Numbers
# https://leetcode.com/problems/sum-root-to-leaf-numbers/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        #     self.sum = 0

        #     def DFS(node, curr_sum):
        #         if not node:
        #             return

        #         curr_sum *= 10 + node.val
        #         if not node.left and not node.right:
        #             self.sum += curr_sum
        #         else:
        #             DFS(node.left, curr_sum)
        #             DFS(node.right, curr_sum)

        #     DFS(root, 0)
        #     return self.sum

        # Not using NONLOCAL

        def DFS(node, curr_sum):
            if not node:
                return 0

            curr_sum = curr_sum * 10 + node.val
            if not node.left and not node.right:
                return curr_sum
            else:
                return DFS(node.left, curr_sum) + DFS(node.right, curr_sum)

        return DFS(root, 0)
