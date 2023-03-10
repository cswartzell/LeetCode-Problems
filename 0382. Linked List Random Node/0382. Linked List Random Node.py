# 03-09-2023 Leetcode 382. Linked List Random Node
# https://leetcode.com/problems/linked-list-random-node/description/

# Man do I hate singly linked lists. Its not 1978. Just include two damned pointers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from random import randint


class Solution:
    head = None
    num_nodes = 0

    def __init__(self, head: Optional[ListNode]):
        self.head = head

        # Get number of nodes on init. KEEP UPDATED on modifiying so this
        # it isnt necessary to iterate the whole list again
        temp = head
        while temp:
            self.num_nodes += 1
            temp = temp.next

    def getRandom(self) -> int:
        rando = random.randint(0, self.num_nodes - 1)
        temp = self.head
        # if not temp:
        #     return -1
        for _ in range(rando):
            temp = temp.next
        return temp.val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
