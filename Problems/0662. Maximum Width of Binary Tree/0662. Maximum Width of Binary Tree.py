# 04-26-2023 Leetcode 662. Maximum Width of Binary Tree
# https://leetcode.com/problems/maximum-width-of-binary-tree/description/

# BFS and count

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        next_row = collections.deque([(1, root)])
        ans = 1
        while next_row:
            ans = max(ans, next_row[-1][0] - next_row[0][0])
            curr_row = next_row
            next_row = collections.deque()
            while curr_row:
                node_idx, curr_node = curr_row.popleft()
                if curr_node.left:
                    next_row.append((2 * node_idx, curr_node.left))
                if curr_node.right:
                    next_row.append((2 * node_idx + 1, curr_node.right))
            if next_row:
                ans = max(ans, next_row[-1][0] - next_row[0][0] + 1)

        return ans
