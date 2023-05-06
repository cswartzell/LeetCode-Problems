# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        # l1 = ListNode()
        # l2 = ListNode()
        summedlist = ListNode()
        carry = 0

        # this actually should have failed as it doesnt sum 2 single valued lists
        while l1.next != None or l2.next != None:
            summedlist.val = l1.val + l2.val + carry
            if summedlist.val > 9:
                summedlist.val % 10
                carry = 1
            else:
                carry = 0

        return summedlist


summylist = Solution()
print(summylist.addTwoNumbers([1, 2, 3, 4], [5, 9, 8, 5]))


"""03-09-2022 Second try without looking at first soltion"""
# sum_list = ListNode(0, None)
# head_holder = ListNode(0, sum_list)
# carry = 0
# while l1 or l2:
#     if l1:
#         sum_list.val += l1.val
#     if l2:
#         sum_list.val += l2.val
#     carry = sum_list.val // 10
#     sum_list.val %= 10
#     if l1:
#         l1 = l1.next
#     if l2:
#         l2 = l2.next
#     if l1 or l2 or carry != 0:
#         sum_list.next = ListNode(carry, None)
#         sum_list = sum_list.next
# return head_holder.next
