# 12-10-2022 Leetcode 124. Binary Tree Maximum Path Sum
# https://leetcode.com/problems/binary-tree-maximum-path-sum/description/



# First of all, it is using a btree as an undirected graph, with the added
# rule that we cannot traverse an edge twice. Since we can head both directions
#on the tree, its just a graph

#I guess we just DFS and start summing "up" from the children
#Each child should only be considered if its pathsum is positive,
#otherwise it should be zero. 

#We also have the weird case that, as a graph, we can start at a leaf, 
#travel up as much as wed like, then travel down to another leaf.
#This means any nodes sum could potentially include the pathsums of both
#of its children, making this node the "peak" of this up, then down path
#We'll need to keep a nonlocal variable to track the max pathsum found yet

#So we Post Order DFS to get down to the leaves, then compare the curr val
#with the sum of the curr nodes left and right children (we are thus effectively
#Searching for the peak path). If we find a childpathsum is negative, we should 
#return zero, effectively claiming we will not be taking any of that path.
#using this a peak could be solo, or include one or both children. 
#As its DFS, we'll figure out the children pathsums first, then work our
#way up the roots, checking every node eventually. 



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = -1001
        def postDFS(root):
            nonlocal max_sum
            if not root:
                return 0
            left = max(postDFS(root.left), 0)
            right = max(postDFS(root.right), 0)
            sub_max = max(left, right) + root.val
            max_sum = max(max_sum, root.val + right + left)
            return sub_max
        

        postDFS(root)
        return max_sum