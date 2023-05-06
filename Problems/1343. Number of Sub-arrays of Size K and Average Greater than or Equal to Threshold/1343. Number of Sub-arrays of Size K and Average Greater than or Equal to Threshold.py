# 03-03-2023 Leetcode 1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
# https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/description/

# Boy... how do we do this? "Generate them all, descending" seems like the obvious,
# yet likely stupid answer. We can do like a rolling hash SORT of thing so its
# LESS calculation, but its still going to be an O(n**2) answer.
# Ok, we ARE looking for unique subarrays. So no funny choose n of k business
# for repetitions.

# Well... we can do SOME elimination. Not sure if its worth it. We dont need more
# than k copies of any int, so we can delete extras.

# If we start at the minimum, and build our way up using a sorted list, then we
# can shorten the elements of the array that will work for us?

# OH! A subarray is contiguous, its SUBSEQUENCE that order matters, but you can skip
# elements. This is now just a sliding window rolling sum thing

# If I just divide every element by k to begin with, I can just sum as I go with no
# further division. Because its not sorted, we will end up dividing all n numbers
# Wait, cant I reverse this and simply MULTIPLY the threshold by k to start?
# This way im summing ints instead of floats, and performing NO division

# AHA! Thats a clever insight. NICE basic math skills.


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        threshold *= k
        start, end = 0, k - 1
        curr_sum = sum(arr[:k])
        subs = 1 if curr_sum >= threshold else 0

        # while end < len(arr) - 1:
        #     curr_sum -= arr[start]
        #     start += 1
        #     end += 1
        #     curr_sum += arr[end]

        #     if curr_sum >= threshold:
        #         subs += 1

        # return subs
        for i in range(len(arr) - k):
            curr_sum += -arr[i] + arr[i + k]
            # subs += 1 if curr_sum >= threshold else 0
            if curr_sum >= threshold:
                subs += 1

        return subs

        # way inefficient 1 line:
        # Oh good, the brute force method actually failed
        # return sum(1 for i in range(len(arr)-k+1) if sum(arr[i:i+k])/k >= threshold)
        # return sum(1 for i in range(len(arr)-k+1) if sum(arr[i:i+k]) >= threshold*k)
