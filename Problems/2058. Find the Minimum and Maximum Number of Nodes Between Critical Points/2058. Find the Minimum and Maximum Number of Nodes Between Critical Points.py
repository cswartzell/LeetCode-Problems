# 04-20-2023 Leetcode 2058. Find the Minimum and Maximum Number of Nodes Between Critical Points
# https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        min_dist, max_dist = math.inf, -1
        dist_first_crit, dist_last_crit = -1, -1
        twoback = oneback = nunback = head
        while nunback.next:
            dist_first_crit += 1 if dist_first_crit >= 0 else 0
            dist_last_crit += 1 if dist_last_crit >= 0 else 0
            twoback, oneback, nunback = oneback, nunback, nunback.next
            if (twoback.val > oneback.val and oneback.val < nunback.val) or (
                twoback.val < oneback.val and oneback.val > nunback.val
            ):
                if dist_first_crit < 0:
                    dist_first_crit = 0
                    continue
                elif dist_last_crit < 0:
                    dist_last_crit = dist_first_crit

                min_dist = min(min_dist, dist_last_crit)
                dist_last_crit = 0
                max_dist = dist_first_crit

        return [min(min_dist, max_dist), max_dist]
