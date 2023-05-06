# 12-08-2022 Leetcode 1026. Maximum Difference Between Node and Ancestor
# https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description/


# If Im not mistaken, this is a DFS where we track min and max
# seen so far in the traversal, then, when at a leaf node
# return the abs of the difference. We should check max
# on every call so we keep the LARGETS difference


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# COMMIT


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def DFS(root, amax, amin, vdif):
            if not root:
                return vdif
            vdif = max([vdif, abs(amax - root.val), abs(amin - root.val)])
            amax = max(amax, root.val)
            amin = min(amin, root.val)
            return max(
                DFS(root.right, amax, amin, vdif), DFS(root.left, amax, amin, vdif)
            )

        return DFS(root, root.val, root.val, 0)
