"""4-20-2022 LeetCode 102. Binary Tree Level Order Traversal"""

from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        output = []
        new_level = deque(
            []
        )  # deque should be a lot faster than using a list as a stack, particularly as we need to popleft (IE A Stack)
        old_level = deque([])
        old_level.append(root)
        while old_level:
            output_level = []
            while old_level:
                root = old_level.popleft()
                output_level.append(
                    root.val
                )  # tried using list as stack, but list.pop pops right... Oh. It takes an index. list.pop(0) IS popleft
                if root.left:
                    new_level.append(root.left)
                if root.right:
                    new_level.append(root.right)
            output.append(output_level)
            old_level = new_level  # shallow copy. Default assignment "isnt" by reference, yet the end up pointing to same object
            new_level = deque([])
        return output
