# 03-05-2024 Leetcode 0141. Linked List Cycle
# https://leetcode.com/problems/linked-list-cycle/?envType=daily-question&envId=2024-03-06

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None or head.next == None:
            return False
        slow, fast = head, head.next
        while fast:
            if fast == slow:
                return True
            if fast.next:
                fast = fast.next.next
            else:
                break
            slow = slow.next    
        return False
