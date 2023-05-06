# 04-26-2023 Leetcode 1008. Construct Binary Search Tree from Preorder Traversal
# https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        # root = TreeNode(preorder[0])
        # # pre_root = TreeNode(0, root, root)

        # def construct_tree(parent_node,  G_max, curr_idx) -> Optional[TreeNode]:
        #     while curr_idx < len(preorder):
        #         if preorder[curr_idx] < parent_node.val:
        #             parent_node.left = TreeNode(preorder[curr_idx])
        #             curr_idx = construct_tree(parent_node.left, parent_node.val, curr_idx + 1)
        #         elif  preorder[curr_idx] < G_max:
        #             parent_node.right = TreeNode(preorder[curr_idx])
        #             curr_idx = construct_tree(parent_node.right, G_max, curr_idx + 1)
        #         else:
        #             return curr_idx
        #     return curr_idx

        # construct_tree(root, math.inf, 1)
        # return root
        root = TreeNode(preorder[0])
        stack = [root]
        idx = 1
        # curr_node = stack[-1]
        while idx < len(preorder):
            curr_node = stack[-1]
            while stack and stack[-1].val < preorder[idx]:
                curr_node = stack.pop()
            if curr_node.val < preorder[idx]:
                curr_node.right = TreeNode(preorder[idx])
                stack.append(curr_node.right)
            else:
                curr_node.left = TreeNode(preorder[idx])
                stack.append(curr_node.left)
            idx += 1

        return root
