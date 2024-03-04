# 03-03-2024 Leetcode 19. Remove Nth Node From End of List
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/?envType=daily-question&envId=2024-03-03
# Time: 15 Challenge: 3/10 READ IT. Nth from END

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        list_len = 0
        curr_node = head
        while curr_node:
            curr_node = curr_node.next
            list_len += 1

        n = list_len-n

        dummy_node = ListNode()
        dummy_node.next = head
        prev_node = dummy_node
        curr_node = head
        while n >= 1 and curr_node:
            prev_node, curr_node = curr_node, curr_node.next
            n -= 1

        if not curr_node:
            prev_node.next == None
        else:
            prev_node.next = curr_node.next
        return dummy_node.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
#         dummy = ListNode(-1, head)
#         curr = head
#         tail = dummy

#         while curr:
#             if not n:
#                 tail = tail.next
#             curr = curr.next
#             n = max(n-1, 0)
        
#         tail.next = tail.next.next if tail.next else None
#         return dummy.next
