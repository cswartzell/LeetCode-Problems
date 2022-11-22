import collections
import heapq

# Hmm... not sure what the obvious method is. If there are big gaps
# In the tree NEXT might be a node diferentiated many branches previous.
# My first guess is: Traverse in level order and build a list.
# Note how many nodes are in each level. Traverse again using these two
# pieces of info to assign next.

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: "Node") -> "Node":
        if not root:
            return

        curr_lvl = deque()
        curr_lvl.appendleft(root.right)
        curr_lvl.appendleft(root.left)

        while curr_lvl:
            righter = curr_lvl.pop()
            next_lvl = deque()
            next_lvl.appendleft(righter.right)
            next_lvl.appendleft(righter.left)
            while curr_lvl:
                lefter = curr_lvl.pop()
                next_lvl.appendleft(lefter.right)
                next_lvl.appendleft(lefter.left)
                lefter.next = righter
                righter = lefter
            curr_lvl = copy.copy(next_lvl)

        return root


#         if not root:
#             return

#         curr_lvl = deque()
#         if root.right:
#             curr_lvl.appendleft(root.right)
#         if root.left:
#             curr_lvl.appendleft(root.left)

#         while curr_lvl:
#             righter = curr_lvl.pop()
#             next_lvl = deque()
#             if righter.right:
#                 next_lvl.appendleft(righter.right)
#             if righter.left:
#                 next_lvl.appendleft(righter.left)
#             while curr_lvl:
#                 lefter = curr_lvl.pop()
#                 if lefter.right:
#                     next_lvl.appendleft(lefter.right)
#                 if lefter.left:
#                     next_lvl.appendleft(lefter.left)
#                 lefter.next = righter
#                 righter = lefter
#             curr_lvl = copy.copy(next_lvl)

#         return root
