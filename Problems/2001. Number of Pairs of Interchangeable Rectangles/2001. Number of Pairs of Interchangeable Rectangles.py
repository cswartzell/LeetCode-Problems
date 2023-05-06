# 03-06-2023 Leetcode 2001. Number of Pairs of Interchangeable Rectangles
# https://leetcode.com/problems/number-of-pairs-of-interchangeable-rectangles/description/

# Just reduce each rectangle to the GCD of w and h, then count em?


class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        # Oh, i is STRICTLY less than j. So not only do they need to reduce to the same amount,
        # but have to have been in some order to begin with. So instead of a set,
        # we just count them and then its combinatronics right? If there are N rectangles for a given
        # ratio class, its just N choose 2 right? But N choose 2 is always just N*N-1
        # We then just sum these combinations

        # return sum(n*(n-1)//2 for n in collections.Counter([(w//math.gcd(w,h), h//math.gcd(w,h) ) for w,h in rectangles]).values())

        return sum(
            n * (n - 1) // 2
            for n in collections.Counter([w / h for w, h in rectangles]).values()
        )
