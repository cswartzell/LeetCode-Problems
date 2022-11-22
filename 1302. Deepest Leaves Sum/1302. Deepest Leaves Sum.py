# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        # A little cleaner

        leaves_sum = root.val if root else 0
        curr_lvl = []
        next_lvl = [
            root
        ]  # a tricksy skip. not having this had me double up assignments and loops
        while next_lvl:
            curr_lvl = next_lvl
            next_lvl = []
            for node in curr_lvl:
                if node.right:
                    next_lvl.append(node.right)
                if node.left:
                    next_lvl.append(node.left)

        return sum(
            node.val for node in curr_lvl
        )  # also tricky: if there are no nodes, the sum WILL be zero


#         curr_lvl = [root]
#         next_lvl = []
#         if root.right:
#             next_lvl.append(root.right)
#         if root.left:
#             next_lvl.append(root.left)

#         while next_lvl:
#             leaves_sum = 0
#             curr_lvl = copy.copy(next_lvl)
#             next_lvl = []
#             while curr_lvl:
#                 node = curr_lvl.pop()
#                 leaves_sum += node.val
#                 if node.right:
#                     next_lvl.append(node.right)
#                 if node.left:
#                     next_lvl.append(node.left)

#         return leaves_sum
