# 02-12-2023 Leetcode 1523. Count Odd Numbers in an Interval Range
# https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/description/

# Fairly trivial and I did more examples when maybe just thinking on it
# might have been enough, but good enough

# Lets investigate possibilities:
# Note: low and high can be equal
# even Even
# Rounding up is same
# 2,2:0   2,4:1  6,12:3    0,20:
# 2-2 = 0 // 2 = 0
# 4-2 = 2 // 2 = 1
# 12-6 = 6 // 2 = 3
# 20-0 = 20 // 2 = 10

# even odd
# 2,3  2,5  6,13   0,21
# 3-2 = 1 / 2 = 1 if rounded up. ZERO IF INT DIV
# 5-2 = 3 / 2 = 2 if rounded up. Correct.
# 13-6 = 7/2 = 4 if rounded up. Correct
# 21-0 = 21 /2 = 11 Correct

# odd even
# 3,4  3,6  7,14  1,20
# 4-3 = 1 / 2 rouned up = 1 Correct
# 6-3 = 3 / 2 rouded up = 2 Correct
# 14-7 = 7 / 2 rounded up = 4 correct
# 20-1 = 19 / 2 = 10 correct

# odd odd
# Round up AND add 1
# 3,3  3,7  7,15  1,21
# 3-3 = 0/2 DOES NOT equal 1 regardless
# 7-3 = 4 /2 = 2 when it should be 3
# 15-7 = 8/2 = 4 when it should be 5
# 21-1 = 20 /2 = 10 when it should be 11


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return int((high - low) / 2 + 0.5 * (high % 2) + 0.5 * (low % 2))
