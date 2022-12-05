# 12-05-2022 Leetcode 876. Middle of the Linked List
# https://leetcode.com/problems/middle-of-the-linked-list/

# nothing to it but O(1.5n), iterate once to count and again
# to the midpoint. Oh, int division rounded up

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # guarenteed to be at least 1
        num_nodes = 1
        og_head = head
        while head.next:
            num_nodes += 1
            head = head.next
        head = og_head
        for i in range(num_nodes // 2):
            head = head.next

        return head
