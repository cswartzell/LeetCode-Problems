03-13-2023 958. Check Completeness of a Binary Tree
https://leetcode.com/problems/check-completeness-of-a-binary-tree/description/ 

# This is a medium? Trivial BFS n check right?
# No. A bunch of possible errors:
# 1) obviously each row  other than the last shuld be 2*row# - 1 long
# Its if we encounter a short row it OUGHT to then be the last row, something
# a flag to TRUE for "weve seen a short row". If we get into the loop again,
# it means there is another row to process and we are done, as the short row then
# violates the rule
# 2) we can NEVER have a node with a right that doesnt also have a left
# 3) FOR the last row, elements must have left AND right until the first one
# to be missing one or the other. After this element, the remainder cant have
# any children at all. Again set a flag for "weve seen the last parent in this row"
# and if we find another node that has children, we know its False. 


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        # I really prefer the two array BFS over the counter queue method. 
        # I dont think its significantly less effecient, the assignment
        # form next to curr is just a reference. Not sure how costly
        # resetablishing next = [] is. Its not deleting the old list
        # as its now assigned to curr, so again it should just be reference change
        # Presumably creating a blank list is fast, but it IS something.
        # I find it clearer though.
        num_nodes = 1
        short_row = False
        next_row = [root]
        
        while next_row:
            if short_row:
                return False
            if len(next_row) != num_nodes:
                short_row = True
            num_nodes *= 2
            
            curr_row = next_row
            next_row = []
            last_parent = False
            for node in curr_row:
                if (node.right or node.left) and last_parent: 
                    return False
                if (node.left and not node.right) or (not node.left and not node.right):
                    last_parent = True
                if node.right and not node.left:
                    return False
                if node.left:
                    next_row.append(node.left)
                if node.right:
                    next_row.append(node.right)        
        
        return True
            
