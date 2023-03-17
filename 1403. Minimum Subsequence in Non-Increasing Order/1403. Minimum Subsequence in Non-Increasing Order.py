# 03-16-2023 Leetcode 1403. Minimum Subsequence in Non-Increasing Order
# https://leetcode.com/problems/minimum-subsequence-in-non-increasing-order/description/

# Boy thats a mouthfull huh? But I think the answer is trivial:
# We can start by summing the current array. We then sort the array.
# Now we want to start building our subsequence. We need it to rapidly
# hit a threshold, using the minimum number of elemend FROM the first array.
# This simply means "grab the largest remaining number and see if the
# subsequence is now complete". If we append them to the subsequence, then
# they are already added in non increasing order. An almost trivial Solution
# to a wordy problem

# Oof I got lucky and avoided a fools trap. Or really faux trap?
# It asks for a subsequence and by starting with sorting I immediately
# destroyed the possibility of getting a subsequence. The LAST step
# of the problem asks you TO sort your subsequence though, so the order
# on WHERE you sort it is irrelevant; it is clearly thus to do it this way.
# The key here being that I did NOT reason my way through this. I ignored
# the subsequence clause, got lucky it didnt matter after all, THEN spotted it.


class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        # nums.sort()
        # nums_sum = sum(nums)
        # subs = []
        # subs_sum = 0

        # #No need to check nums not empty, as the condition WILL be false before
        # #trying to pop a num thats not there
        # while subs_sum <= nums_sum:
        #     x = nums.pop()
        #     nums_sum -= x
        #     subs_sum += x
        #     subs.append(x)

        # return subs

        # Interesting. WAY slower. For loops suck I guess. Youd think Popping vals would
        # take more time than merely iterating them

        nums.sort(reverse=True)
        nums_sum = sum(nums)
        subs = []
        subs_sum = 0

        # No need to check nums not empty, as the condition WILL be false before
        # trying to pop a num thats not there

        for x in nums:
            nums_sum -= x
            subs_sum += x
            subs.append(x)

            if subs_sum > nums_sum:
                return subs

        # NEVERMIND, the absolute fastest answer is LITERALLY identical to the above except var names:

    #     class Solution:
    # def minSubsequence(self, nums: List[int]) -> List[int]:
    # summ = sum(nums)
    # nums.sort(reverse=True)
    # ans = []
    # new_sum = 0
    # for num in nums:
    #     new_sum += num
    #     summ -= num
    #     ans.append(num)
    #     if summ < new_sum:
    #         return ans
    # return [0]
