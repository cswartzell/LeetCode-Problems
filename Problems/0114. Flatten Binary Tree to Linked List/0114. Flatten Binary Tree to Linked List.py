# 05-02-2023 Leetcode 114. Flatten Binary Tree to Linked List
# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/

# It seems trivial to do it as a seperate list. Just traverse and build

#How to do in place?
# go down left until end: mark as curent end.
# go UP until there is a right. Move to the left of the current end.
# repeat until you reach root and there are no more rights
# Damn. Now its a linked list of lefts.
# I guess go down whole list and reverse this




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return root

        stack = []
        currNode = root
        endNode = root

        # while stack:
        while True:
            #Go to the end leftmost node, mark as end
            while currNode.left:
                stack.append(currNode)
                currNode = currNode.left
            endNode = currNode

            # Start backtracking til you find a right
            while stack and not currNode.right:
                currNode = stack.pop()
            #add to end of chain, on the left. Delete
            if currNode.right:
                endNode.left = currNode.right
                currNode.right = None
            # Or, if no rights found, we are done
            else: 
                break

        #reverse list
        currNode = root
        while currNode.left:
            currNode.left, currNode.right = None, currNode.left
            currNode = currNode.right
        
        return root
            
