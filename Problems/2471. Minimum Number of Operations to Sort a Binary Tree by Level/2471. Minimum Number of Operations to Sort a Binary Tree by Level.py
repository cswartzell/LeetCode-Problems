# 03-03-2024 Leetcode 2471. Minimum Number of Operations to Sort a Binary Tree by Level
# https://leetcode.com/problems/minimum-number-of-operations-to-sort-a-binary-tree-by-level/
# Time: 30 Challenge: 5/10: Kinda went down a rabbit hole. I actually do think my 
# Union Find method would work, but was overly complex. Just actually doing the swaps
# was more reasonable

# bfs levelwise... then what?
# Ok, heres what I got: each node, if incorrect, has exactly one directed edge.
# the out edge for where its current val goes. Every node has one out, and will have
# an incoming edge from its correct val from some other node.
# In the case of only two nodes being swapped, they point to eachother. In this case
# it takes just one swap. If there are three nodes, they MUST form a kind of triangle,
# for if they didnt, they'd be 2 incorrect nodes pointing to eachother, which makes the
# third node correct. We make our first swap, and as its all symetric, the order doesnt 
# matter. There are no real choices. Now the three node situation becomes the two node
# situation, and is solved with one more swap. 

# One hypothesis is that we can simply extend this, and incorrect nodes will form a ring
# of len n and it takes n-1 swaps to fix the ring. A large amount of incorrect nodes could
# form multiple, disjoint rings. This would be an ideal case for union find. UF, count members
# per ring, sum needed swaps. Is this necessarily true? I had to keep going with examples.

# Now imagine 4 nodes. We have some choices. Put them in a square. One class of possibilities 
# is 2 sets of pairs (imagine parallel lines horizontal, parallel vertical, and an X shape for
# the edges). This class requires TWO swaps and we are done. 

# Another posibility is the simple square ring, flowing either direction. This
# gives us two trivial classes as seen before. What about an hour glass shape, is that different?
# I think not. All the nodes are identity less as the system is symetric. We could "pick up" the 
# hourglass and untwist it and itd just be a square again. All of these SHOULD take 3 swaps right?

#There are seemingly the only two classes of shapes. The number of missing nodes however might take
# different numbers of swaps based on how many rings they form

# This makes sense, there is no such thing as a terminal node for that would mean it has what... an
# out edge but no in edge or vice versa? If its val is wrong, it must go somewhere AND recieve its
# corrected val. nodes can ONLY connect in a sort of ring, and once the ring is closed, it is 
# satisfied. No extra edge can enter the ring or leave from it to connect to another shape. 

# Disjoint unions it is? Seems valid, but fairly complicated for a medium


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        ans = 0        
        next_lvl = [root]

        while next_lvl:
            curr_lvl = next_lvl
            next_lvl = []
            vals = []

            for node in curr_lvl:
                vals.append(node.val)
                if node.left:
                    next_lvl.append(node.left)
                if node.right:
                    next_lvl.append(node.right)

            curr_sorted = sorted(vals)
            idx_of = {val:idx for idx, val in enumerate(vals)}

            for idx in range(len(vals)):
                if vals[idx] != curr_sorted[idx]:
                    swap_idx = idx_of[curr_sorted[idx]]
                    vals[idx], vals[swap_idx] = curr_sorted[idx], vals[idx]
                    idx_of[vals[idx]] = idx
                    idx_of[vals[swap_idx]] = swap_idx
                    ans += 1
        return ans

# class Solution:
#     def minimumOperations(self, root: Optional[TreeNode]) -> int:
#         ans = 0        
#         next_lvl = [root]
        
#         def root(x:int) -> int:
#             while idx_roots[x] != x:
#                 idx_roots[x] = roots(idx_roots[x])
#             return idx_roots[x]

#         def union(x:int, y:int):
#             root_x = root(x)
#             root_y = root(y)
            
#             if root_x < root_y:
#                 idx_roots[y] = root_x
#             else:
#                 idx_roots[x] = root_y

#         def reroot():
#             for idx in range(len(idx_roots)):
#                 idx_root[idx] = root(idx)

#         def swap_count()
#             counts = collections.Counter(idx_roots).values()
#             return sum(x-1 for x in counts)

#         while next_lvl:
#             curr_lvl = next_lvl
#             next_lvl = []

#             curr_sorted = sorted(curr_lvl)
#             correct_idx = {val:idx for idx, val in enumerate(curr_sorted)}
#             idx_of_idx = 


#             idx_roots = [x for x in range(len(curr_lvl))]


#             for node in curr_lvl:
#                 if node.left:
#                     next_lvl.append(node.left)
#                 if node.right:
#                     next_lvl.append(node.right)