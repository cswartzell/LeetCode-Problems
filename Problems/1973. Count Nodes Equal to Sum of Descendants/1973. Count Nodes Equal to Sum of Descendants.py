    # 02-29-2024 Leetcode 1973. Count Nodes Equal to Sum of Descendants
# https://leetcode.com/problems/count-nodes-equal-to-sum-of-descendants/?envType=weekly-question&envId=2024-02-29
# Time: 15 mins Challenge: 2/10



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def equalToDescendants(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def DFS(node) -> int:
            if not node:
                return 0
            
            descendant_sum = DFS(node.right) + DFS(node.left)
            if node.val == descendant_sum:
                self.ans += 1

            return descendant_sum + node.val

        DFS(root)
        return self.ans