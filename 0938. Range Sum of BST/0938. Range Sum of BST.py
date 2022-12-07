# 12-06-2022 Leetcode 938. Range Sum of BST
# https://leetcode.com/problems/range-sum-of-bst/description/

#simple


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        def sum_it(root):
            if not root:
                return 0
            sumd = root.val if low <= root.val <= high else 0 
            return sumd + sum_it(root.right) + sum_it(root.left)

        return sum_it(root)
