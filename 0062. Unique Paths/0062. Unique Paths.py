# 12-27-2022 Leetcode 62. Unique Paths
# https://leetcode.com/problems/unique-paths/?envType=study-plan&id=level-1

# There's got to just be a math solution to this
# ok, so its Pascals Traingle rotated such that the
# "finish" mark is the head of the triangle. Somehow this is useful.
# I guess I could just write a pascals triangle generator, generate the
# min(rows, cols) layer, then use the max(rows,cols) element for the answer.
# Im certain theres got to be a one shot way of doing this however.

# We could of course DP it and just build each cell from the one below it, plus
# the one to the right. Fill the right col and bottom row with 1 to start,
# We can do this with a single row instead of a MxN grid

# I KNEW it was combinatronics (Binomial Coefficients), Somehow
# C(m,n) in some form. Its just C(m-1 + n-1 , m-1) here


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # mnmax = max(m, n)
        # mnmin = min(m,n)

        # dp = [1]*(mnmin)
        # for _ in range(mnmax-1):
        #     for i in range( (mnmin - 2), -1, -1 ):
        #         dp[i] += dp[i+1]

        # return dp[0]

        # return math.factorial(m+n-2)//((math.factorial(m-1))*(math.factorial(n-1)))
        return math.comb(m + n - 2, m - 1)
