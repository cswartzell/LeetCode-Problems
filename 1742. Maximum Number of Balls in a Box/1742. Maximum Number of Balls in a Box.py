# 02-08-2023 Leetcode 1742. Maximum Number of Balls in a Box
# https://leetcode.com/problems/maximum-number-of-balls-in-a-box/description/

# I wracked my brains for hours thinking there may be a mathematical solution.
# I noted that, like dice, you will end up with a normal distribution summing
# the individual digits: For two digits for instance, they sum to 10 most often
# 1+9, 2+8, 3+7... 8+2, 9+1. This can be extended for more digits and holds, but
# given the start and end can be left off I think you just have to calculate it.
# I even discovered a cycle thing, you add one to each of 10 sums in a row, then
# go up one box, and repeat another 10. 0,1,2...9,1,2,3....10,11,12....

# Its simple just to use a counter and convert and count them. Useful to note that
# there are only 45 possbile sums, 0+0+0+0+0...9+9+9+9+9. Not QUIET O(1)but given
# contraints you can figure out the max.


class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        # count = collections.defaultdict(int)
        # for i in range(lowLimit, highLimit + 1):
        #     count[sum([int(x) for x in str(i)])] += 1
        # return max(count.values())

        return max(
            collections.Counter(
                [sum([int(x) for x in str(i)]) for i in range(lowLimit, highLimit + 1)]
            ).values()
        )
