# 04-17-2023 Leetcode 1302. Deepest Leaves Sum
# https://leetcode.com/problems/deepest-leaves-sum/

#BFS and sum final row? Is that it? Seems trivial

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
#         next_row = [root]
#         while next_row:
#             curr_row = next_row
#             next_row = []
#             for node in curr_row:
#                 if node.left:
#                     next_row.append(node.left)
#                 if node.right:
#                     next_row.append(node.right)
        
#         return sum(node.val for node in curr_row)

class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode], lvl=0, sum_per_lvl=defaultdict(int)) -> int:
        sum_per_lvl[lvl] += root.val if root else 0
        
        if root.left:
            self.deepestLeavesSum(root.left, lvl+1, sum_per_lvl)
        if root.right:
            self.deepestLeavesSum(root.right, lvl+1, sum_per_lvl)
        
        if lvl == 0:
            anskey = max(sum_per_lvl.keys())
            ans = sum_per_lvl[anskey]
            return ans