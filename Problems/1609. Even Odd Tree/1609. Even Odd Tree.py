# 02-29-2024 Leetcode 1609. Even Odd Tree
# https://leetcode.com/problems/even-odd-tree/?envType=daily-question&envId=2024-02-29
# Time: 15 mins Challenge: 2/10

# BFS Levelwise. Simple

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        next_lvl = [root]
        lvl_parity = 0

        while next_lvl:
            curr_lvl = next_lvl
            next_lvl = []
            lvl_parity ^= 1
            curr_max = 10**6 + 1
            curr_min = 0
            for node in curr_lvl:
                if node.val % 2 != lvl_parity:
                    return False
                if lvl_parity == 1:
                    if node.val <= curr_min:
                        return False
                    curr_min = node.val
                else:
                    if node.val >= curr_max:
                        return False
                    curr_max = node.val
                if node.left:
                    next_lvl.append(node.left)
                if node.right:
                    next_lvl.append(node.right)

        return True