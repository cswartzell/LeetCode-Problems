# 02-17-2023 Leetcode 226. Invert Binary Tree
# https://leetcode.com/problems/invert-binary-tree/description/

# Famous one isnt it? Also, pointless.
# Lets go recursive as I think its easier, and there are only 100 nodes
# so the tree is only 7 layers deep. Oh hey. First try. TY Python


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(
                root.left
            )
        return root
