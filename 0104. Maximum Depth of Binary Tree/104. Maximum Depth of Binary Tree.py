# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
if root is None:
    return 0

max_depth = 1
stack = []
stack.append((max_depth, root))

while stack != []:
    curr_depth, curr_node = stack.pop()
    max_depth = max(max_depth, curr_depth)
    if curr_node.left != None:
        stack.append((curr_depth + 1, curr_node.left))
    if curr_node.right != None:
        stack.append((curr_depth + 1, curr_node.right))
print(max_depth)
