"""04-21-2022 LeetCode 0094. Binary Tree Inorder Traversal"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) if root else []

        stack = []
        output = []
        while stack or root is not None:
            while root is not None:
                stack.append(root)
                root = root.left
            root = stack.pop()
            output.append(root.val)
            root = root.right
        return output
