# 12-07-2022 Leetcode 34. Find First and Last Position of Element in Sorted Array
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

# "Do two binary searches". I think. Is there a more creative way to get info on
# TWO parameters at once? At least for a bit I guess: if the range is entirely above
# or below on our initial splits we CAN use that info. Once our pivot point splits
# the range, its two binary searches from there

# Id really love to learn the syntax for pythons automated binary search, but then again
# should really start by writing this from scratch for the first try to make sure I can

# Python has a list method that gets the index of the first occurance of an item in a list.
# I suspect it does so via Binary Search, so there is a language feature that can just do
# this for us, but obviously we shouldnt rely on that


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        rng_begin_lo = 0
        rng_begin_hi = len(nums) - 1
        rng_end_lo = 0
        rng_end_hi = len(nums) - 1

        # Binary Search "leftmost target"
        # if mid is a target, move the rightmost pointer to it, and
        # continue searching. Mid should evenutally be just one below
        # hi, then low will be moved to hi and we can exit: hi will be leftmost
        while rng_begin_lo < rng_begin_hi:
            mid = (rng_begin_lo + rng_begin_hi) // 2
            if nums[mid] < target:
                rng_begin_lo = mid + 1
            elif nums[mid] > target:
                rng_begin_hi = mid - 1
            else:
                rng_begin_hi = mid
        pass

        # same principal as above to find rightmost target
        # NOTE! The trick is the ceil function to make sure mid creeps
        # RIGHT as we continue to refine our search. // would make mid
        # tend to fall left, which was failing.
        while rng_end_lo < rng_end_hi:
            mid = math.ceil((rng_end_lo + rng_end_hi) / 2)
            if nums[mid] < target:
                rng_end_lo = mid + 1
            elif nums[mid] > target:
                rng_end_hi = mid - 1
            else:
                rng_end_lo = mid
                # rng_end_hi -= 1
        pass

        if nums[rng_begin_hi] != target or nums[rng_end_lo] != target:
            return [-1, -1]

        return [rng_begin_hi, rng_end_lo]

        # mid at least now is pointing to a copy of the target
        # I think this calls for a sort of weird new binary search: find the leftmost/rightmost

        # while rng_begin_lo <= rng_begin_hi:
        #     mid = (rng_begin_lo + rng_begin_hi) // 2
        #     if nums[mid] < target:
        #         rng_begin_lo = mid + 1
        #     else rng_begin_hi = mid - 1
