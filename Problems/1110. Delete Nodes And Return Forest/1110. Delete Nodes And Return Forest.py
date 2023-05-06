# 03-20-2023 Leetcode 1110. Delete Nodes And Return Forest
# https://leetcode.com/problems/delete-nodes-and-return-forest/description/

# DFS POST ORDER: if upon returning to node (after L, R), node IS
# in to_delete, add L, R to ans. else carry on.
# At the end, if original root is not in too delete, add original root
# Should be the only special case. We could also start with this check

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def delNodes(self, root: Optional[TreeNode], to_d: List[int]) -> List[TreeNode]:
        if not root:
            return []

        # Stupid to keep running through a list. Convert to hash
        to_delete = set(to_d)
        forrest = []

        def DFS_PO(node):
            show_forrest = forrest
            if not node:
                return
            DFS_PO(node.left)
            DFS_PO(node.right)

            if node.val in to_delete:
                if node.left and node.left.val not in to_delete:
                    forrest.append(node.left)
                if node.right and node.right.val not in to_delete:
                    forrest.append(node.right)
                node.left = None
                node.right = None
            else:
                if node.left and node.left.val in to_delete:
                    node.left = None
                if node.right and node.right.val in to_delete:
                    node.right = None

        DFS_PO(root)
        if root.val not in to_delete:
            forrest.append(root)

        return forrest
