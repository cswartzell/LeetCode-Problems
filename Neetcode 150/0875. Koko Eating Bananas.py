# 11-13-2023 Neetcode 875. Koko Eating Bananas
# https://leetcode.com/problems/koko-eating-bananas/
# time: 30 mins

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_bananas = max(piles)
        return bisect.bisect_left(range(max_bananas + 1), True, 1, key = lambda m: h >= sum(math.ceil(pile/m) for pile in piles))


# # 03-07-2023 Leetcode 875. Koko Eating Bananas
# # https://leetcode.com/problems/koko-eating-bananas/description/

# #Im going to go with a binary search on this. Same problem as
# #https://leetcode.com/problems/minimum-time-to-complete-trips/editorial/
# #We can attempt to do better on our initial bounds

# #She only eats from one pile AT MOST per hour, but we are told that
# #len(piles) <= h. Our upper bound is  the LARGER number of bananas per hour
# #Lets just set this to len(piles) * largest_pile. We might be able to better, but
# #this is kind of a worst case. Similarly, I cant figure out a better lower bound other 
# #than 1. Interesting, because of the limit of working on at most one pile at a time, we
# #cant do clever math like I did for the bus problem to tighten our bounds


# class Solution:
#     def minEatingSpeed(self, piles: List[int], h: int) -> int:
#         smallest_pile, largest_pile = min(piles), max(piles)
#         upperbound = largest_pile
#         lowerbound = 1

#         return bisect.bisect_left(range(max(piles)), True, 1, key= lambda mid: sum(math.ceil(pile/mid) for pile in piles) <= h)
#         # return bisect.bisect_left(range(max(piles) + 1), True, 1, key=lambda mid: sum(math.ceil(pile/mid) for pile in piles) <= h)

#         #Man, its so hard recognizing the various off by one pitfalls that always come with Binary Search.
#         #Id never write this without reference in a real situation. I mean, Id pick BS for sure but Id look
#         #at guides for creating them

#         # while lowerbound <= upperbound:
#         #     mid = (lowerbound + upperbound)//2
#         #     hours_taken = sum(math.ceil(pile/mid) for pile in piles)
#         #     if hours_taken <= h:
#         #         upperbound = mid - 1
#         #     else: 
#         #         lowerbound = mid + 1
        
#         # return upperbound + 1
