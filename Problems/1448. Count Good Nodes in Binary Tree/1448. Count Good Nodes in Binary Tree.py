# 03-03-2023 Leetcode 1448. Count Good Nodes in Binary Tree
# https://leetcode.com/problems/count-good-nodes-in-binary-tree/description/

# Medium? Isnt this just DFS and pass the max down? Keep a global variable
# and add to it? Am I missing something?
# Im just going to go preorder: this node result, then down left, then right
# Return nothing at a leaf

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_num) -> int:
            if not node:
                return 0
            return (
                dfs(node.left, max(max_num, node.val))
                + dfs(node.right, max(max_num, node.val))
                + int(node.val >= max_num)
            )

        return dfs(root, -10001)
