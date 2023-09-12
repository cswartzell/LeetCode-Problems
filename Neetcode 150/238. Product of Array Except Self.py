# 09-11-2023 Neetcode 238. Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/description/
# Time: 45 mins. Just barely


# First, we may want to count how many zeros there are;
# if there are 2 or more zeros, the whole ans is [0,0,...,0]
# If its just one, then ans is [0,0,0,PROD OF THINGS OTHER THAN ZERO, 0, 0]
# with that prod being where the zero is.

# else, its all just product and is all good.

# AH! Is it something like prefix product AND suffix product arrays,
# then multiply the two as we go

# DOUBLE AHA! We dont need to calculate the postfix! We can just accumulate it
# as we go, multiplying the accumulated number to the calculated prefix array.
# doing so allows us to back fill our computed prefix array with postfix multiplying
# and thus we only use one array, and a single accumulate int: as output magically
# doesnt count for space complexity, this is O(1)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        for i in range(1, len(nums)):
            prefix.append(nums[i-1]*prefix[i-1])
        accumulate_right = 1
        for i in range(len(nums)-1,-1,-1):
            prefix[i] *= accumulate_right
            accumulate_right *= nums[i]

        return prefix

        # prefix = [1]
        # for i in range(1, len(nums)):
        #     prefix.append(nums[i-1]*prefix[i-1])
        # postfix = [1] * len(nums)
        # for i in range(len(nums)-2,-1,-1):
        #     postfix[i] = postfix[i+1] * nums[i + 1]

        # return [prefix[i] * postfix[i] for i in range(len(nums))]
        
        # zero_at_i = -1
        # for i, num in enumerate(nums):
        #     if num == 0:
        #         if zero_at_i == -1:
        #             zero_at_i = i
        #         else:
        #             return [0] * len(nums)
        # if zero_at_i != -1:
        #     lzp = 1
        #     for num in nums:
        #         lzp = lzp * num if num != 0 else lzp
        #     return [0 if idx != zero_at_i else lzp for idx in range(len(nums))]
        # prod =  1
        # for num in nums:
        #     prod *= num
        # return [prod//num for num in nums]
