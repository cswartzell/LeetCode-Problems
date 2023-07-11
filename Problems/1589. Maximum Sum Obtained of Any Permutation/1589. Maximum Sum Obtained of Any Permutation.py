# 07-10-2023 Leetcode 1589. Maximum Sum Obtained of Any Permutation
# https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/description/

# First instict: Make a parallel array times_requested where we track for each index 
# that element was requested. As its all additive, order doesnt matter. So after
# processing all the requests we would know "index 5 was requested 8 times
# and index 4 was requested 2 times". We then sort this array AND the nums array
# in descending order. We no longer care about indexes: we will know the most requested
# index got requested X times, so we should assing it the highest num possible. The 
# second most requested index should get the second highest num etc.
# This clearly maximizes the sum of sums of requests.
class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        times_requested = [0 for _ in range(len(nums)+1)]
        # for start, stop in requests:
        #     for i in range(start, stop + 1):
        #         times_requested[i] += 1
        
        for L, R in requests:
            times_requested[L] += 1
            times_requested[R+1] -= 1 
        
        for i in range(1, len(times_requested)):
            times_requested[i] += times_requested[i-1]

        times_requested.sort(reverse=True)
        nums.sort(reverse=True)

        # return sum((times * value) % 10**9 + 7 for times, value in zip(times_requested, nums))

        ans = 0
        i = 0
        while i < len(times_requested) and times_requested[i]:
            ans += (nums[i] * times_requested[i])
            ans %= (10**9 + 7)
            i += 1
        
        return ans