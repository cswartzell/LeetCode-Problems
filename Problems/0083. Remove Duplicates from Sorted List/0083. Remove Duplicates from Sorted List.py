# 12-09-2022 Leetcode 83. Remove Duplicates from Sorted List
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        curr_node = head
        curr_head = curr_node
        next_node = curr_node

        while next_node:
            next_node = next_node.next
            while next_node and next_node.val == curr_node.val:
                next_node = next_node.next
            curr_node.next = next_node
            curr_node = curr_node.next

        return curr_head
