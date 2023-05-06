# 03-15-2023 1485. Clone Binary Tree With Random Pointer
# https://leetcode.com/problems/clone-binary-tree-with-random-pointer/

# First of all, I think we are going to have to parse it twice.
# Ignoring for a second HOW to connec the rando pointer, obsiously we
# cant have it point to a node we havent created yet. So step 1 is going to
# be just to make a straight copy of the structure using dual parallel BFS

# Now... how to track to the random pointers? The values arent unique so we cant
# use that to just make a map. The example images rather unhelpfully list "index no."
# for each node, but there is no real index data to be seen. I could cheat and
# wrap the exiting node class to add an index, then iterate through the existing
# tree and give all nodes indecies. Then when creating our tree give the same indecies
# and create a parallel dict that stores a pointer to each index. THEN wed BFS the
# original tree and see what index points to which index and parallel BFS our copy
# and pull the same route out of our dict. This seems quite cumbersome for a medium.
# Not to mention, it doesnt seem ideal to modify the existing tree.

# Wow, a little stumped otherwise. The WHOLE POINT of a tree structure like this is to
# NOT need a map with all the connections. Each node only knows where its children are
# and thats it. Any given node has no info about the rest of the entire structure.
# Sure, it can point to some other random node, but it has no idea where in the
# tree that is.

# WAIT. They DO have unique "indexes". The random pointer isnt a pointer to a node,
# but an integer that points to a nodes implicit index. Indecies being implied copyRandomBinaryTree
# BFS traversal. This INCLUDES nodes that dont exist. We skip their indecies as if they did.
# BUT the nodes themselves dont store this index information.


# Ok, well then it IS just make a dict with these phano


# Definition for Node.
# class NodeCopy:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random


class Solution:
    def copyRandomBinaryTree(self, root: "Optional[Node]") -> "Optional[NodeCopy]":
        if not root:
            return None

        copy_dict = dict()
        new_root = NodeCopy()
        copy_dict[root] = NodeCopy()

        next_row_orig, curr_row_orig = [root], []
        next_row_copy, curr_row_copy = [new_root], []

        while next_row_orig:
            curr_row_orig, next_row_orig = next_row_orig, []
            curr_row_copy, next_row_copy = next_row_copy, []

            # while curr_row_orig:
            #     curr_node_orig = curr_row_orig.pop()
            #     curr_node_copy = curr_row_copy.pop()

            #     curr_node_copy.val = curr_node_orig.val

            #     if curr_node_orig.left:
            #         if curr_node_orig.left not in copy_dict:
            #             copy_dict[curr_node_orig.left] = NodeCopy()
            #         curr_node_copy.left = dict[curr_node_orig.left]
            #         next_row_orig.append(curr_node_orig.left)
            #         next_row_copy.append(curr_node_copy.left)

            #     if curr_node_orig.right:
            #         if curr_node_orig.right not in copy_dict:
            #             copy_dict[curr_node_orig.right] = NodeCopy()
            #         curr_node_copy.right = dict[curr_node_orig.right]
            #         next_row_orig.append(curr_node_orig.right)
            #         next_row_copy.append(curr_node_copy.right)

            #     #Random does NOT get added to any sort of queue. Ostensibly we are hitting all the nodes
            #     #in the tree via BFS already, so it either has already been filled out in full, or will
            #     # in the near future anyhow
            #     if curr_node_orig.random:
            #         if curr_node_orig.random not in copy_dict:
            #             copy_dict[curr_node_orig.random] = NodeCopy()
            #         curr_node_copy.random = dict[curr_node_orig.random]

        return copy_dict[root]


# class Solution:
#     def __init__(self):
#         # Hashmap to map old tree's nodes with new tree's nodes.
#         self.new_old_pairs: dict[str, int] = {None: None}

#     def deep_copy(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
#         if not root:
#             return None
#         new_root = NodeCopy(root.val)
#         # Deep copy left subtree and attach it on new node's left.
#         new_root.left = self.deep_copy(root.left)
#         # Deep copy right subtree and attach it on new node's right.
#         new_root.right = self.deep_copy(root.right)
#         # Store the new node and old node's pair in hash map.
#         self.new_old_pairs[root] = new_root
#         return new_root

#     def map_random_pointers(self, old_node: 'Optional[Node]') -> None:
#         if not old_node:
#             return
#         new_node = self.new_old_pairs[old_node]
#         old_node_random = old_node.random
#         new_node_random = self.new_old_pairs[old_node_random]
#         # Map newNode with it's respective random node.
#         new_node.random = new_node_random
#         # Traverse on rest nodes to map their respective new node's random pointers.
#         self.map_random_pointers(old_node.left)
#         self.map_random_pointers(old_node.right)

#     def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
#         # Create a new tree for each node of old tree and map new node with old respective node.
#         new_root = self.deep_copy(root)
#         # We will assign random pointers of new tree to respective correct new nodes.
#         self.map_random_pointers(root)
#         return new_root
