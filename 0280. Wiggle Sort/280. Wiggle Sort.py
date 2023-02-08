# 02-07-2023 Leetcode 280. Wiggle Sort
# https://leetcode.com/problems/wiggle-sort/description/

# I mean... naively I can just sort it, then transpose pairs right?
# that'd be O(n log n) for the sort, so an additional pass of O(n)
# swapping isnt really worse. I can do it in place for O(1) space.

# There may be more 'clever' solutions, but they will almost certainly
# be some form of sorting so how can you beat this? Why?

# Ok, the hint asks "can this be solved in O(n)" so it must be possible
# I guess anything is O(n) using bucket sort and enough buckets...


# Ok lets think logically: looking at a pair of numbers there are only 3
# possibilities: They are the same, so leave them. The first is larger than
# the second, or the second is larger than the first. We need to flip flop
# back and forth on larger smaller larger smaller, and can safely ignore pairs
# of identical numbers.

# lets start at the begninning: we need the first number to be smaller than the
# second. If it isnt, then the OPPOSITE is true. If we swap these two, then the
# condition is satisfied. Now we have a small number followed by a bigger number.
# NOW we need the second number to be larger than the third. If it is, or the smame,
# great. If not we know the third number is EVEN BIGGER than the second, meaning
# its BIGGER YET than the first. We can safely swap 2 and 3, knowing the relationship
# where 1 is smaller than 2 will hold. Now [2] IS larger than [3]
# Ok. So now we definitely have [1] < [2] > [3]
# Lets look at [3] and [4]. We want [3] to be smaller than [4]. Using the same logic,
# if it is already true or they are the same, move on. If not, then [4] is SMALLER
# than [3], Which means its smaller than [2]. We can swap [3] and [4] knowing the
# relationship for [2] to [4] will hold as intended


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # nums.sort()
        # for i in range(1, len(nums)-1, 2):
        #     nums[i], nums[i+1] = nums[i+1], nums[i]

        # Shocking. The O(n) solution is slower than the O(n logn) solution
        for i in range(1, len(nums)):
            if i & 1:
                if nums[i] < nums[i - 1]:
                    nums[i], nums[i - 1] = nums[i - 1], nums[i]
            else:
                if nums[i] > nums[i - 1]:
                    nums[i], nums[i - 1] = nums[i - 1], nums[i]
