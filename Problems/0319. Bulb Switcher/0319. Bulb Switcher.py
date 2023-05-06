# 05-01-2023 Leetcode 319. Bulb Switcher
# https://leetcode.com/problems/bulb-switcher/editorial/

#How many factors under n? if even, off, if odd, on
#We COUNT 1 and itself as a factor, except in the case of "1" where we dont double count it
# in fact, no double counting. 2 is a factor of 4, but only once

# for x we only need to check how many factors are between 0 and x, and we can assume 2, 
# counting 1 and x itself anf only check [2...x-1]
# We could use DP, and when we find a factor, include all that factors factors?

#And really if we count the 1 and x, we know its next highest factor is at most x//2
# so check factors [2,x//2 + 1]? or better yet, [2...sqrt(x)]
# And we dont need to add the assumed 2 for 1 and x themselves, we only care if its even or
# odd, and so adding 2 doesnt change the parity

# n= 10**9. This is clost to an O(n**2) solution... 

#OH NICE. So I am on the right track, a bulb is left on if it has an odd number of factors
# off otherwise. Heres the trick. Every number will have an even number of factors under n
# unless it is a perfect square. take 80: its divisible by 1 and 80 of course, so we add TWO
# factors. Its divisible by 2 and 40 so we add TWO factors. We are always adding factors in pairs
# UNLESS its the square root, as we dont double count

# we simply count the number of perfect squares in n, inclusive!

class Solution:
    def bulbSwitch(self, n: int) -> int:
        # if n < 2:
        #     return n
        # if n == 2:
        #     return 1
        # ans = 0
        # for x in range(3, n +1):
        #     factors = 1
        #     for i 0
        #     .in range(2, math.ceil(sqrt(x)) + 1):
        #         factors += x % i == 0
        #     ans += factors & 1

        # return ans

        # return sum( 1 for x in range(1, math.floor(sqrt(n)) + 1)  if x**2 <= n)
        #Bottom 8%?! For a one Line?! This is a GREAT solution. 

        #Oh shit, of course! If floor(sqrt(n)) is less than n, and it must be, then 
        #of course it also contains all the smaller squares!
        # So for example, 26. floor(sqrt(26)) = 5, so 5**2 is in it. So 4**2 must be
        # and 3**2 and 2**2 and 1**1... conviniently that IS 5 square roots. Its its own counter!
        # The answer is just:
        return math.floor(sqrt(n))