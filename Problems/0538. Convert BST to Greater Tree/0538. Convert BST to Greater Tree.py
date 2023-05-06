# 04-05-2023 Leetcode 538. Convert BST to Greater Tree
# https://leetcode.com/problems/convert-bst-to-greater-tree/description/

# Right to left in-order, add right child val to curr val right?


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def RLinorder(total, node) -> int:
            if node is None:
                return total
            total = RLinorder(total, node.right)
            node.val += total
            return RLinorder(node.val, node.left)

        RLinorder(0, root)
        return root
