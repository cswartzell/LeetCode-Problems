"""4-21-2022 Leetcode 230. Kth Smallest Element in a BST"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        # This is an iterative method, useful to stop searching once found
        # We could use the more simple recursive method and generate the full
        # list of the B Tree, but that might be very wasteful
        stack = []
        while True:
            # find the smallest node (leftest)
            while root:
                stack.append(root)
                root = root.left
            # pop and ignore it, until we've popped off k of them
            root = stack.pop()
            k -= 1

            if k == 0:  # if this our kth round of ignoring, return this val
                return root.val
            root = root.right
