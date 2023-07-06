# 07-05-2023 1493. Longest Subarray of 1's After Deleting One Element
# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/description/

# First instinct thats not O(n**2) is a little sloppy:
# Kind of a prefix sum thing. List each zero, but collapse all consecutive
# ones into a single count. Then sliding window of triples simply looking for the
# biggest sum. Reason this is slopy is if the list is of len one or two we have 
# special cases. Lets list them:

# len 1: all zeros- list will be [0], return 0
# len 1: all ones- list will be [#of1s], return #of1s - 1
# len 2: must be [0, #] or [#, 0] for it must contain a mix or it would be
# a list of len 1. In either case just return the # as we can delete the zero
# len 3+: there must be alternating 0s and #s, such that there is a max
# [0,#,0] or [#,0,#]. In either case we can delete (one of) the zero(s).
# This can be done by summing the triple in the case of [#,0,#] and return

#I guess this list is short enough to just code? 

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # sumd = []
        # i = 0
        # while i < len(nums):
        #     if nums[i] == 0:
        #         sumd.append(0)
        #         i += 1
        #     else:
        #         count = 0
        #         while i < len(nums) and nums[i] == 1:
        #             count +=1
        #             i += 1
        #         sumd.append(count)

        # if len(sumd) == 1:
        #     if sumd == [0]:
        #         return 0
        #     else:
        #         return sumd[0] -1
        # elif len(sumd) == 2:
        #     # return max(sumd)
        #     return sum(sumd)

        # ans = 0
        # for i in range(len(sumd)-2):
        #     ans = max(ans, sumd[i]+sumd[i+1]+sumd[i+2])        
        # return ans

        ans = 0
        prev, curr = 0, 0

        for x in nums:
            if x == 0:
                ans = max(ans, prev + curr)
                prev, curr = curr, 0
            else: 
                curr += 1

        if prev == 0 and ans == 0:
            return curr if nums[0] == 0 else curr - 1 
        else:
            return max(ans, prev + curr)
