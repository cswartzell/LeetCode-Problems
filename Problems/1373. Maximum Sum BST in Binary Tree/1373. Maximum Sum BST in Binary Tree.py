# 03-16-2023 Leetcode 1373. Maximum Sum BST in Binary Tree
# https://leetcode.com/problems/maximum-sum-bst-in-binary-tree/

# Hmmm. Instinct is this doesnt seem that hard. Need to pass UP a tuple
# though, conaining both the sum of what is below  AND if everything in
# the child node DOWN is still a btree. If a nodes child is NOT a btree
# then the curent node is not one. All nodes DEFAULT to being b-trees
# until a comparison of their children is made, THEN this is modified
# by the return on their children


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional


class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        def bst(node):
            # if not node:
            #     return True, 0

            this_is = True
            if node.left and node.left.val >= node.val:
                this_is = False
            if node.right and node.right.val <= node.val:
                this_is = False

            if not node.left:
                left_is = True
            left_is, left_sum = bst(node.left)
            right_is, right_sum = bst(node.right)

            if left_is and right_is and this_is:
                return True, left_sum + right_sum + node.val
            else:
                return False, max(left_sum, right_sum)

        _, ans = bst(root)
        return ans
