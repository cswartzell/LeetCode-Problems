# 04-17-2023 Leetcode 513. Find Bottom Left Tree Value
# https://leetcode.com/problems/find-bottom-left-tree-value/description/

# This should be an easy
# BFS, when not next row, return curr_row[0]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        next_row = collections.deque([root])
        left_most = None  # We are guarenteed there is one node, so will get overwritten with at least root
        # However, this is BETTER as if there WASNT a node, itd still be right
        while next_row:
            curr_row = next_row
            next_row = collections.deque()
            left_most = curr_row[0].val
            while curr_row:
                curr_node = curr_row.popleft()
                if curr_node.left:
                    next_row.append(curr_node.left)
                if curr_node.right:
                    next_row.append(curr_node.right)

        return left_most
