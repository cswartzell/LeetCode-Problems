# 12-05-2022 Leetcode 41. First Missing Positive
# https://leetcode.com/problems/first-missing-positive/

# with O(n) time and constant space sorting is out nor can we keep
# track of seen nor mark out expexted

# well, we can keep track of lowest int series seen so far. Namely, we
# want to see "1", otherwise the answer is simply 1.

# We can just ignore negative numbers. We may need to count how many
# occurances of negative numbers weve seen (and 0) so we can get the len
# of the positive ints in the array

# Can we use the triangular number sum to help? If only ONE number was
# missing, of course. But multiple numbers could be missing and we are
# only interested in the lowest of these
# sum of ints * 2 = X * (X + 1), have to use quadratic formula, but A
# and B are simplified so its just
# (-1 + sqrt(1-4*(-sum)))/2

# We can then compare the actual sum to the expected sum of n numbers
# to see the difference... I dont know if this is going anywhere.
# This difference is then the SUM of the missing numbers

# it cant be a monotonic stack thing right? That wouldnt be O(n)

# Had to look it up. I dont love it. I did recognize that we could just
# ignore 0 and negative numbers, that could have been the hint; If we
# KNOW our list is then all positive numbers, we can "cheat" and use
# the sign bit of the input to store information about n nodes. Thus
# my instinct was correct, it CANT be done without n storage, but there
# is a way to sneak that storage in without it being "additional".
# I think this solution is clever, but its absolutely not obvious and to
# ask someone to come up with this without a hint is kind of trash.


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # first pass: clear the negative numbers and zero.
        nums = [x for x in nums if x > 0]

        # second pass: start marking found ints. This is the "clever"
        # bit: the first missing int must be below n itself; if the list WASNT
        # missing an int, then it must contain 1-n, so there is no room for numbers
        # larger than n. A single number larger than the length of the list will imply
        # there is a missing number. Also any double. But a larger number is of no further
        # utility, we dont need to store info about it. We only need to store infor about
        # numbers UNDER n, and hey— now we have a data structure of len n to do so
        for num in nums:
            if abs(num) <= len(nums):
                nums[abs(num) - 1] *= -1 if nums[abs(num) - 1] > 0 else 1

        # Note this is destructive to the input, which is some bullshit.
        # Now I could just multiply these by minus one instead, which would
        # allow me to reverse the proccess later. I could have sorted the list in
        # the beginning and only started this process with the positive half of the list
        # too, thus also preserving the negative ints and zeros at the cost of a few
        # pointers.

        missingno = len(nums) + 1
        for n in range(len(nums)):
            if nums[n] > 0:
                missingno = n + 1
                break
        return missingno

        # print(int((-1 + math.sqrt(1-4*-90))/2))
