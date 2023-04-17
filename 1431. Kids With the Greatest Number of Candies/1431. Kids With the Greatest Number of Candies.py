# 04-16-2023 Leetcode 1431. Kids With the Greatest Number of Candies
# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/description/


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        return [kid_haul + extraCandies >= (m := max(candies)) for kid_haul in candies]
        # m=max(candies)
        # return [kid_haul + extraCandies >= m for kid_haul in candies]
