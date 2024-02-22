# 02-21-2024 Leetcode Daily 201. Bitwise AND of Numbers Range
# https://leetcode.com/problems/bitwise-and-of-numbers-range/?envType=daily-question&envId=2024-02-21
# Time: 25 Challenge: 5/10

# A real logic puzzle. I started thinking about this in base 2 and came
# up with the following, but its easier to understand in base 10: if the 
# start and stop are even ONE digit appart, then of course the ones digit
# will change. As we are anding all the numbers, this means it will be 0.
# Now, for base 10, if the difference is at least 10 appart, then the tens
# digit MUST change. The same in base 2.  Say the two are more than 8 appart,
# then the 4th bit, the 2^3rd bit, will HAVE to change. Any bits over this 
# may change. Possibly only the very next bit? If I start with 1002 and go
# to 1015, the ones and tens changed, the hundreds were both 0 to start with
# but the thousands anded together would be a 1. 

# use log to find the power of the bits that MUST change. I think we can do
# ceil(log2(max(start, stop) - min(start,stop)) + 0.5). We need to round up 
# as in the 2^3 being for the FOURTH digit. Or just zero index I guess. 
# right shift off that many digits, then left shift back to zero them out.
# Then simply and the start and stop? 
# Test case binary: 11111101 - 11111111. The first 6 match. The 1s digit
# APPEARS to match naively, but we know using the above it will be anded off
# I think this works? 

import math


class Solution:
    def rangeBitwiseAnd(self, l: int, r: int) -> int:
        if l == r: 
            return l
        shift = floor(log2(r-l)) + 1
        r_shifted = (r>>shift<<shift)
        return l & r_shifted

        #
        