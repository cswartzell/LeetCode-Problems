# 07-18-2023 Leetcode 445. Add Two Numbers II
# https://leetcode.com/problems/add-two-numbers-ii/description/

# Options: 
# Reverse the list, add backwards
# Abuse Pythons unlimited int and just add both up, then add them together
# Store each digit in an array. Add arrays, w/ripple carry

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Store list 1 in array
        list1 = []
        while l1:
            list1.append(l1.val)
            l1 = l1.next
        # Store list 2 in array
        list2 = []
        while l2:
            list2.append(l2.val)
            l2 = l2.next

        # Make list1 the longest of the two. Add an index to catch final carry
        if len(list1) < len(list2):
            list1, list2 = list2, list1
        list1 = [0] + list1

        # Add digits of list2 to list1, ripple carrying
        i = len(list1) - 1
        while list2:
            list1[i] += list2.pop()
            if list1[i] > 9:
                list1[i] -= 10
                list1[i-1] += 1
            i -= 1

        # Coninue ripple carrying (add extra elemnet if needed. Is it ever?)
        while i >= 0 and list1[i] > 9:
            if i == 0:
                list1 = [1] + list1
                break
            list1[i] -= 10
            list1[i-1] += 1
            i -= 1
            
        # Truncate added index if leading zero
        if list1[0] == 0:
            list1 = list1[1:]

        # Create and return a new list
        new_list = ListNode()
        prev = new_list
        for digit in list1:
            prev.next = ListNode(digit)
            prev = prev.next

        return new_list.next