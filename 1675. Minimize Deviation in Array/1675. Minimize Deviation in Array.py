

#I wonder if i should store them all as tuples and include their original val

#Ok, so any odds have only two states: themeselves, and themsleves*2
#I THINK the baseline is the HIGHEST odd number doesnt change. At least not at first
 
#We need to find out if max odd is in our extant odds, or if one of the large evens is going
# to be larger. We start by seperating the two into two sorted lists. If the last element of evens
# is greater than twice the last element of odds, we know THAT will be break down to be our max odd

#... but we dont asssume we want to break it? do we?

from collections import deque

class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:

        # min_deviation = 10**9 + 1
        # min_val = 10**9 + 1
        # max_val = 0
        # heap = []

        # for i in range(len(nums)):
        #     if nums[i] & 1:
        #         heapq.heappush(heap, -(nums[i] * 2))
        #         min_val = min(min_val, nums[i] * 2)
        #     else: 
        #         heapq.heappush(heap, -(nums[i]))
        #         min_val = min(min_val, nums[i])

        # while True:    
        #     top = -1 * heapq.heappop(heap)
        #     min_deviation = min( min_deviation, top - min_val)
        #     if top & 1:
        #         return min_deviation
        #     else:
        #         heapq.heappush(heap, top // -2)
        #         min_val = min(min_val, top // 2)
        





        # # nums.sort()
        # # moved = True

        # # while moved:
        # #     moved = False
        # #     if not nums[-1] & 1 and (
        # #         (nums[-1] // 2) >= nums[0] or nums[-2] - (nums[-1]//2) < nums[-1] - nums[0]
        # #     ):
        # #         nums = sorted(nums[: len(nums) - 1] + [nums[-1] // 2])
        # #         moved = True
        # #     if nums[0] & 1 and (
        # #         (nums[0] * 2) < nums[-1] or (nums[0] * 2) - nums[1] < nums[-1] - nums[0]
        # #     ):
        # #         nums = sorted(nums[1:] + [nums[0] * 2])
        # #         moved = True

        # # return nums[-1] - nums[0]






        # evens, odds = [], []
        # max_odd = 0
        # bottom = 500001
        # top = 1
        # for num in nums:
        #     if num & 1:
        #         odds.append(num)
        #     else:
        #         evens.append(num)
        #         while not num & 1:
        #             num >>= 1
        #     bottom = min(bottom, num)
        #     top = max(top, num)
        #     max_odd = max( max_odd, num)
        
        # num_ops =0
        # odds.sort()
        # evens.sort()       

        # threshold = (2/3) * max_odd
        # for num in odds:
        #     if num < b

        # # num_ops = sum(1 for x in odds if x * 3/2 < max_odd)
        # threshold = (4/3) * max_odd
        # for num in evens:
        #     while num > threshold:
        #         num_ops += 1
        #         num >>= 1
        
        # return num_ops


        # # if 3/2*new_odd < max_odd //multiply small odd by 2