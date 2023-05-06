# 03-16-2023 106. Construct Binary Tree from Inorder and Postorder Traversal
# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/

# Uh oh. This sounds tough. Well, tough if you are a little hazy
# on the subject. It just doesn't click for me as much as many other cs elements.
# Off the bat I note the firs element is the left most first leaf. Doesnt mean its
# in the bottom row though. I guess we sort of start building from there?

# The two orderings are very different so Im going to have to use some relational
# mapping to figure out the structure. Im sure its actually relatively simple, but
# I dont immediately see it. Lets rubber duck it out:

# In Order: Left, Parent, Right. Post Order: Left, Right, Parent

# So lets start with the array[0]. If this isnt the same, then I guess we're fucked?
# If they are the same, boom. One node down, create it. If there is more array, then this
# guy has a parent. If postOrder[1] == inorder[2], then the previous created node is the
# Parent. Create it, and set our previously made node as its left. Now to check our
# new parent node and see if it has a right. If postorder[2] == inorder[1] thats a right.
# Create it, add it to our parent. Weve just made a little fork. Yay.

# While it seems trivial, its important to note a parent cannot be null. If we have a child,
# obiously we have a parent. For in order, the parent immediately follows
# the let child in the array, whil for post order it follors the right.

# Since we  KNOW our very first node is a left leaf (or the trivial solitary root),
# we then can say for certain using Inorder what its parent is, inorder[2]. If the THIRD element
# of inorder is null we have a little left leg, parent, and no right and are also
# done and able to move up a step.

# If inorder has a right, we've got more tree to go...third element of inorder may be
# way the hell down this right subtree. We are going to need info from Postorder.
# Ok, but we DO have our current parent, and in post order the value immediately PRECEEDING
# our match to parent is this parents right node. Cool. We can than push this as a potential
# parent of OTHER nodes that may be further right.

# So I guess we need a stack of "expecting parents". Lets also maybe make the input lists
# hashes or deques so we can pop off vals once we are sure weve made that node.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def helper(in_left, in_right):
            # if there is no elements to construct subtrees
            if in_left > in_right:
                return None

            # pick up the last element as a root
            val = postorder.pop()
            root = TreeNode(val)

            # root splits inorder list
            # into left and right subtrees
            index = idx_map[val]

            # build right subtree
            root.right = helper(index + 1, in_right)
            # build left subtree
            root.left = helper(in_left, index - 1)
            return root

        # build a hashmap value -> its index
        idx_map = {val: idx for idx, val in enumerate(inorder)}
        return helper(0, len(inorder) - 1)
