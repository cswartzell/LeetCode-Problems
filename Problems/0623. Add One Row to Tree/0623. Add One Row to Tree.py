# 04-15-2024 Leetcode 623. Add One Row to Tree
# https://leetcode.com/problems/add-one-row-to-tree/?envType=daily-question&envId=2024-04-16
# time: 10mins Challenge:3/10

class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, root, None)

        def recurse(node, curr_depth):
            if not node:
                return

            if curr_depth < depth - 1:
                recurse(node.left, curr_depth + 1)
                recurse(node.right, curr_depth + 1) 
            else:
                node.left = TreeNode(val, node.left, None)
                node.right = TreeNode(val, None, node.right)
                
        recurse(root, 1)
        return root




# #Boy some of these mediums now seem super easy
# #this is a pretty straight-forward BFS, and just
# #do some dumb inserting at a given level. 
# #Oh, iterative of course here. 

# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
#         #Could maybe work this in below, but lets just do a base case for depth == 1
#         #Aww, we cant pass in the existing tree to the constructor? Bah, two lines then

#         # if depth == 1:
#         #     new_root = TreeNode(val)
#         #     new_root.left = root
#         #     return new_root

#         # #find the "split" levels
#         # curr_lvl = []
#         # next_lvl = [root]
#         # while depth > 1 and next_lvl:
#         #     curr_lvl = next_lvl
#         #     next_lvl = []
#         #     for node in curr_lvl:
#         #         if node.left:
#         #             next_lvl.append(node.left)
#         #         if node.right:
#         #             next_lvl.append(node.right)
#         #     depth -= 1

#         # for node in curr_lvl:
#         #     new_node_L, new_node_R = TreeNode(val), TreeNode(val)
#         #     new_node_L.left , new_node_R.right = node.left, node.right
#         #     node.left, node.right = new_node_L, new_node_R

#         # return root

#         #SAME AS ABOVE, but you CAN pass treenodes as args to the constructor?  
#         if depth == 1:
#             return TreeNode(val, root, None)

#         #find the "split" levels
#         curr_lvl = []
#         next_lvl = [root]
#         while depth > 1 and next_lvl:
#             curr_lvl = next_lvl
#             next_lvl = []
#             for node in curr_lvl:
#                 if node.left:
#                     next_lvl.append(node.left)
#                 if node.right:
#                     next_lvl.append(node.right)
#             depth -= 1

#         for node in curr_lvl:
#             node.left, node.right = TreeNode(val, node.left, None), TreeNode(val, None, node.right)
        
#         return root
