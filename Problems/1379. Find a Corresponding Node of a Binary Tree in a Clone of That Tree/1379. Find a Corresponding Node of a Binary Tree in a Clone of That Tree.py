"""05-17-2022 Leetcode 1379. Find a Corresponding Node of a Binary Tree in a Clone of That Tree"""

# What am I missing, this seems absurdly simple. As its an exact clone
# and we are told the values are unique we just perform any tree search
# and return a TreeNode that points to the node of the target value?
# Ok, I need to practice both the iterative AND recursive method, I
# always jump to iterative. Lets try recursive first.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def getTargetCopy(
        self, original: TreeNode, cloned: TreeNode, target: TreeNode
    ) -> TreeNode:
        def dfs(root, clone):
            return (
                clone
                if root == target
                else None
                if not root
                else dfs(root.left, clone.left) or dfs(root.right, clone.right)
            )

        return dfs(original, cloned)
        # def dfs(root, clone):
        #     if not root: #This was an important cognitive step: dont check if root.left exists and
        #                  # If so, call the recursion. Just send it and THEN see if it exists. How odd.
        #                  # Well, root.left DOES exist as it is a variable, a container. It might not have
        #                  # a value (or rather its value is NONE), but we can safely send none. We just cant
        #                  # reference none.anything
        #         return None
        #     if root == target:
        #         return clone
        #     return dfs(root.left, clone.left) or dfs(root.right, clone.right)
        # return dfs(original, cloned)

        #   def dfs(root):
        #     if not root:
        #         return None
        #     if root.val == target:
        #         return root
        #     left = dfs(root.left)
        #     if left:
        #         return left
        #     right = dfs(root.right)
        #     if right:
        #         return right
        #     return None
        # return dfs(cloned)


# Lets sumarize in plain speech:
# IF this node is blank, send back nothing. End this side of the search
# IF this node is our target, send it back: were done
# IF neither of those have occured, then maybe we have some child nodes:
# WITHOUT checking them, lets repeat this process. Send them.
# send the right left half first, then the right half.
# This is PREORDER traversal since we are looking at the root, then L, then R

# NOTE the final return is an OR. it returns the first truthy value.
# If a branch of the left dfs returns NONE, then it returns the value of
# the right branch; either the answer or also none and this branch is dead.
# and we go back to previous calls.
