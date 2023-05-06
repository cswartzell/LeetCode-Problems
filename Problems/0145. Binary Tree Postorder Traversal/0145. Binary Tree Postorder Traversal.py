"""04-21-2022 LeetCode 145. Binary Tree Postorder Traversal"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # if not root:
        #     return None #base case
        # stack = []
        # output = []
        # lastVisit = None #keeps track of right leaves we've already seen
        # while root or stack:
        #     while root:     #stack all left nodes
        #         stack.append(root)
        #         root = root.left
        #     nodePeak = stack[-1] #peak is last pushed
        #     if not nodePeak.right or nodePeak.right == lastVisit: #SKIP if right nodes we havent seen
        #         root = stack.pop()
        #         output.append(root.val) #otherwise weve reached a new leaf, add it to output
        #         lastVisit = root #move seen leaves pointer up to its parent
        #         root = None #weird tricky way to work back up to unpushed brances higher up
        #     else:
        #         root = nodePeak.right # Push right nodes, repeat until leaf right
        # return output
        return (
            self.postorderTraversal(root.left)
            + self.postorderTraversal(root.right)
            + [root.val]
            if root
            else []
        )

    # cool version using a tuple attached to each terminal leaf noting if we've seen it
    # if not root:
    #   return []


#             res=[]
#             stack=[(root,False)]

#             while stack:
#                 node,visited=stack.pop()
#                 if visited:
#                     res.append(node.val)
#                 else:
#                     stack.append((node,True))
#                     if node.right:
#                         stack.append((node.right,False))
#                     if node.left:
#                         stack.append((node.left,False))


#             return res
