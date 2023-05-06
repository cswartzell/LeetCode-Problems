# 12-05-2022 Leetcode 328. Odd Even Linked List
# https://leetcode.com/problems/odd-even-linked-list/

# Well this is the definition of a trick. One I dont know.
# ARE there multiple solutions to this, or is it a singular
# hack? So far I am drawing a blank. I mean... its sinularly
# linked, so we CAN only really process it once... forward.
# We cant use like a two pointer solution as we cannot move
# backwards. I think anything like a circular list would be cheating
# in the sense that its no really O(n) if we loop say n times.
# We cant just save nodes into a list, so we MUST be swapping them...
# somehow. I can easily overwrite the evens to group the odds in O(n)
# but clearly that doesnt work. I can only store what, one even value?
# where do I put it? Cant just make a parallel list, thatd be O(n)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        odd_pointer = head
        even_head = head.next
        even_pointer = even_head

        while even_pointer and even_pointer.next:
            if odd_pointer.next:
                odd_pointer.next = odd_pointer.next.next
            if even_pointer.next:
                even_pointer.next = even_pointer.next.next
                if odd_pointer.next != None:
                    odd_pointer = odd_pointer.next
                even_pointer = even_pointer.next

        odd_pointer.next = even_head
        # even_pointer.next = None

        return head
