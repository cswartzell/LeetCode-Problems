# 07-16-2023 Leetcode 1644. Lowest Common Ancestor of a Binary Tree II
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-ii/description/

#DFS to find P, DFS to find Q. Count depth. 


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def DFS(node, state):
            if not node:
                return [False, False, None] 
            
            found_p = node == p
            found_q = node == q

            left_state = DFS(node.left, state[::])
            right_state = DFS(node.right, state[::])

            if left_state[2]:
                return left_state
            if right_state[2]:
                return right_state

            state[0] = state[0] or found_p or left_state[0] or right_state[0]
            state[1] = state[1] or found_q or left_state[1] or right_state[1]

            if state == [True, True, None]:
                state[2] = node
            
            return state

        return DFS(root, [False, False, None])[2]
        