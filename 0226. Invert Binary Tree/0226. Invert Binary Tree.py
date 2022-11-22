"""05-18-2022 Leetcode #226 Invert Binary Tree"""

# Why is this a meme? Because it sounds hard but is trivial?

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return
        root.right, root.left = root.left, root.right
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
