"""05-01-2022 Leetcode 905. Sort Array By Parity"""
# Ok, so there's two obvious main methods here: One is a linear
# scan and just make two new buckets, then concatenate them at the end
# Thats O(N) and O(N) respectively. We could actually scan and swap values
# sacrificing some time for memory. Probably would use two pointers.
# May as well swap in place with no extra memory while were at it.

# Oh what the hell. Obviously the below was going to be slow, but it 
# only ranked in the 63% for memory, despite only adding two int pointers
nums = [0, 2, 1]

l_i = 0
r_i = 1
while l_i < len(nums) and r_i < len(nums):
    if nums[l_i] % 2 == 1:
        while r_i < len(nums):
            if nums[r_i] % 2 == 0:
                nums[l_i], nums[r_i] = nums[r_i], nums[l_i]
                break
            r_i += 1
    l_i += 1
    if r_i == l_i:
        r_i += 1
print(nums)

# return nums
