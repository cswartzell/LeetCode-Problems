"""03-09-2022 LeetCode 61. Rotate List"""
# I NAILED this one, more or less exactly as the solution describes
# AND I caught many optomizations people suggested in comments.
# I actually didnt see anything I could really do better!


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    if not head or k == 0 or not head.next:
        return head
    length = 0
    head_start = ListNode(0, head)
    while head:
        length += 1
        head = head.next
    k = k % length
    if k == 0:
        return head_start.next
    head = head_start.next
    new_head = 0
    for i in range(length):
        if i + k + 1 == length:
            new_head = head.next
            head.next = None
            head = new_head
        if head.next:
            head = head.next
        else:
            head.next = head_start.next
            break
    return kth_pos


Solution()
