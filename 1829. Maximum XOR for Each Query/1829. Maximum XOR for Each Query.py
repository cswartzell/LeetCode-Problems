# 03-29-2023 leetcode 1829. Maximum XOR for Each Query
# https://leetcode.com/problems/maximum-xor-for-each-query/description/

# What an absolutely jacked up way to ask this.
# First, XOR all the elements in n. Then, xor in one more element, we will call k
# such that the total is the highest. K has to be between 0 and 2**max bit.
# Heres the deal, Xoring the existing list is going to give us a static answer:
# its just some binary number. The way to maximize this is to XOR in a k that
# that fills every zero in this number with a 1. So we want every zero in
# our sum to be filled in with a 1 and we dont want ANY 1 in xor_sum to be
# a 1 in k, or they will cancel out.

# if xor_sum = 00010101 and k can be up to 5 bits, then k should fill those
# two holes:   00001010. Hey, how convinient: this is
#              00001111.
# We can always come up with a k to fill all the zeros such that the xor_sum^K
# is (at least up to the max bit) all filled with 1s. How?
# Set k_prime = 0000011111 where the ones start at the max bit
# now k = xor_sum^k_prime: all the 1s that match in the k section will be turned
# off, and only the 1s that fill the holes in the k section remain. Uh oh, we also
# gain 1s above max bit that ARE on in the xor_sum section (where the are allowed to be)
# Thats ok, we can just AND k with k_prime to get rid of these bonus 1s. Only the
# ones in the k section will be left behind.

# So thats how we come up with K. Now how do we efficiently remove the last element?
# Well... just XOR it again. Xor adds, then removes elements.

# So the full process is:
# compute k_prme = 2**max_bit - 1
# xor the full list: xor_sum = reduce(x^y, nums)
# then, for length (nums)
# compute k:
# k = (xor_sum^k_prime)&k_prime
# append this to the list
# xor out the last element of the list:
# xor_sum^last element


from functools import reduce


class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        # k_prime = 2**maximumBit - 1
        # xor_sum = reduce(lambda x,y: x^y, nums)
        # answer = []
        # for xor_out in nums[::-1]:
        #     answer.append((xor_sum^k_prime)&k_prime)
        #     xor_sum ^= xor_out
        # return answer

        # xor_sum = reduce(lambda x,y: x^y, nums)
        return [
            (xor_sum := reduce(lambda x, y: x ^ y, nums))
            ^ xor_out
            ^ (2**maximumBit - 1) & (2**maximumBit - 1)
            for xor_out in (nums[::-1] + [0])
        ][:-1]
