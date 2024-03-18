# 03-17-2024 Leetcode Challenge 2897. Apply Operations on Array to Maximize Sum of Squares
# https://leetcode.com/problems/apply-operations-on-array-to-maximize-sum-of-squares/
# Time: 45 Challenge: 7/10


# n and k are huge. We most definitely are not doing some massive
# check all the things... I'm guessing 2d dp. 

# First things first, sort the nums. ANDing always produces the same
# number or less. It obviously cannot increase a number. ORing MAY increase
# a number, or may not. No way to know but to do it. But which number 
# should we increase? lets look at [8,17] being ORed with 3.
# thats [0b1000,0b10001] | 0b11. 8 becomes 11 as we gain both bits.
# 17 becomes 19, we only gain the 2^1 bit. Which one was better?
# Before we had 8^2+17^2 = 353. 11^2+17^2=410, 8^2+19^2=425
# So ORing with the 17 was more beneficial, despite it gaining fewer
# bits. Does this ALWAYS hold? Of course not. Lets look at 
#[0b11110,0b10000] | 0b01111. If ORd with the first number it is only 
# increased by 1. If ORd with the second number it gains 15.
#  30^2+16^2=1156, 31^2+16^2=1217, 30^2+31^2=1861

# So its not about which gains more bits, the first example had 17 gain
# fewer bits and still come out on top. Its not about just making the larget
# number, or total amount of increase on a number by number basis... 
# Im not sure if we can be greedy. Backtracking? But n can be huge...

# Can we notice anything abstract about the operations? When (x+a)**2
# is better than (y+b)**2? How do we note which things to try? I have 
# nothing at this point. Like...  literally nothing. 

# AHA! THE UNUSED BITS ARE NOT WASTED! We are ANDing i, which means
# "Take the bits from i that DONT match and add them to j. KEEP the
# bits you dont use. Feel free to use them elsewhere". As we can perform
# any number of operations, this means "Take the k largest numbers and set 
# them aside. Now take all the bits from the remaining numbers and distribute
# them to the k largest, top down"

# Now its just a matter of doing it. 
# Sort nums, possibly actually partition it for ease.
# Do a counter for BIT POSITION. I guess x= 1<<y and
# sum 1 if remaining num AND x for all remaining nums
# Repeate as long as x < remainingnums[-1]
# If we iterate backwards we can early exit.
# Instead of doing a counter we could two pointer and actually
# move the bit to the next K_num that will take it, exit early
# too if we run out of k nums?


# Ah... Almost. Its not just donating bits to K highest, as the example
# [25,52,75,65] k = 4 shows. Do we perform zero operations as we need
# all 4 nums? NO! Moving the bits from the 25 to the 65 will INCREASE
# the sum. We basically want to fill ALL the bits of the highest number.
# Shift EVERY BIT to the rightmost available number. As such we should 
# 0) declare a list of len(k) of all zeros
# 1) count the number of bits per bit position
# 2) OR that many bits, right to left of our ans array, adding those bits
# to the highest existing number. No need to resort, doing it this way
# is stable. 

# We just build up the k nums using the bits we've got. No need to 
# AND out the bits from the list

# While there is not a NEED to sort, we could early exit from checking
# if nums has a given bit position as these grow large. Is it worth it 
# though? Would depend on input. 

class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        ans = [0] * k

        max_num = max(nums)
        iterations = 0
        while max_num:
            iterations += 1
            max_num >>= 1

        bit_position = 1
        for iteration in range(iterations):
            bit_count = sum(1 for num in nums if num & bit_position)
            
            j = k-1
            while j >= 0 and bit_count:
                if not ans[j] & bit_position: 
                    ans[j] |= bit_position
                    bit_count -= 1
                j -= 1
            
            bit_position <<= 1
        
        return sum(x**2 for x in ans) % (10**9 + 7)



        # if len(nums) == 1:
        #     return nums[0]**2

        # nums.sort()

        # rem_nums, K_nums = nums[:len(nums) - k], nums[-k:]

        # donor_bit = 1
        # while donor_bit <= rem_nums[-1]:
        #     i = len(rem_nums) - 1
        #     donor_count = 0
            
        #     #Count donor bits
        #     while i >= 0 and donor_bit <= rem_nums[i]:
        #         if rem_nums[i] & donor_bit:
        #             donor_count += 1
        #         i -= 1

        #     j = len(K_nums) - 1
        #     # Move to K_nums
        #     while j >= 0 and donor_count:
        #         if not K_nums[j] & donor_bit:
        #             K_nums[j] |= donor_bit
        #             donor_count -= 1
        #         j -= 1

        #     donor_bit <<= 1

        # return sum(x**2 for x in K_nums)