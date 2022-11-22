"""4-21-2022 LeetCode 144. Binary Tree Preorder Traversal"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # the following is the non-recursive preorder traversal method

        #         # if root is None:    #I guess lets get the base case out of the way
        #         #     return []       # Ah, it can handle root being null, but not null.right essentially
        #                               # Can indeed be left out if you indent the checks for children
        #                               # As this is specifically preorder, we are hitting roots first so can assume so

        #         stack = [root]
        #         output = []

        #         while stack:
        #             root = stack.pop()
        #             output.append(root.val)
        #             if root.right is not None:
        #                 stack.append(root.right)
        #             if root.left is not None:
        #                 stack.append(root.left)
        #         return output

        return (
            [root.val]
            + self.preorderTraversal(root.left)
            + self.preorderTraversal(root.right)
            if root
            else []
        )
        # while seemingly obvious, I must remember that + for concatenation of list elements is NOT sublists, just
        # comma seperated elements of the same list depth. So even though an empty list is returned, only its CONTENTS
        # get concatenated, not itself: [4] + [7] = [4,7], not [[4],[7]], and thus NOT [4] + [] = [4], not [[4],[]]
