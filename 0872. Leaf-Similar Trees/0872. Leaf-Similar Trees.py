# 12-08-2022 Leetcode 872. Leaf-Similar Trees
# https://leetcode.com/problems/leaf-similar-trees/

# run DFS on each tree, collecting leaves. Compare the two lists


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        # def dfs(node, arr):
        #     if node:
        #         if not node.left and not node.right: arr += [node.val]
        #         dfs(node.left, arr)
        #         dfs(node.right, arr)
        #         return arr

        # return dfs(root1, []) == dfs(root2, [])

        def leaf_it(root, lvs):
            if root:
                if not root.left and not root.right:
                    lvs += [root.val]
                leaf_it(root.left, lvs)
                leaf_it(root.right, lvs)
                return lvs

        return leaf_it(root1, []) == leaf_it(root2, [])
