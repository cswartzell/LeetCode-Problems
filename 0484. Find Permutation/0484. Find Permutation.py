# First guess is you simply count up as you scan index, swapping
# values for each D incountered. I think for multiple Ds you reverse
# the whole block: DDD -> start with [1,2,3,4], reverse the block to
# [4,3,2,1]. IDDIDDD -> [1,2,3,4,5,6,7] -> [1,3,2,4,7,6,5]
# Python reversing ans swapping list slices should be a cinch


# OH WAIT!
# FUCKING Negative SLICES NOT OPERATING ON INDEX 0... The slice is EXCLUSIVE
# of its end point, so you cant have its end point == 0 and get that
# value. Then again, you cant use -1 as the endpoint to capture zero
# either. Its obnoxious to get a reversed slice that includes index zero
# I could just pad in a zero index place holder and
# strip it at the end? Bah, I hate that. Ive used psychotic negative
# number indexing to get around this as the ZERO index is the only
# discontinuity; -n-1 and below behaves just like a repeating ribbon
# so you are free to cross that boundry without weird jumps.

# Huh, Well this two pointer solution works but because of the above
# ugliness with zero index slices I dont love it. Its also not very
# eficcient I think, but not terrible. I really like the stack
# version as its much more straightforward and elegant


class Solution:
    def findPermutation(self, s: str) -> List[int]:
        key = [0] * (len(s) + 2)

        #         test = [0,1,2,3,4,5,6,7,8,9]
        #         test[3:7] = test[6:2:-1]

        # Prime straight list of ordered numbers PADDED WITH ZERO

        # Noting later, I didnt really pad it with zero, but changed it to
        # indexed by one, skipping index zero.

        # Could be done IN the loop as we go for 1 less N pass, but
        # seriously why bother

        for i in range(1, len(key)):
            key[i] = i

        left_d = 0
        right_d = 0

        while left_d < len(s):
            if s[left_d] == "D":
                while right_d < len(s) and s[right_d] == "D":
                    right_d += 1
                key[left_d + 1 : right_d + 2] = key[right_d + 1 : left_d : -1]
                left_d = right_d
            left_d += 1
            right_d = left_d
        return key[1:]
