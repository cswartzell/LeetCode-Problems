"""03-11-2022 Leetcode 138. Copy List with Random Pointer"""

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        head_start = Node(0, head)

        if not head:
            return head

        # create a copy each node immediately following itself, then skip over this
        # new temp node to get to the end of the list. ONLY copies val and sequential]
        # pointer, we have to build this before dealing witht the rando pointers...
        while head:
            clone = Node(head.val, head.next, None)
            head.next = clone
            head = clone.next

        # restart

        head = head_start.next

        # now point the NEXT (dummy) nodes rando to THIS elements rando, or rather
        # the copy of the rando element, allowing us to delete the original list
        while head:
            if head.random:
                head.next.random = head.random.next
            else:
                head.next.random = None
            head = head.next.next

        # restart and point to the head of the dummy list
        head = head_start.next
        head_start = head.next

        # remove all the pointers from the original list, leaving only the new list
        while head:
            jmp = head.next
            try:
                head.next = head.next.next if head.next.next else None
            except AttributeError:
                pass
            head = jmp

        return head_start
