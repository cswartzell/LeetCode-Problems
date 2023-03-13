# 03-12-2023 Leetcode 1954. Minimum Garden Perimeter to Collect Enough Apples
# https://leetcode.com/problems/minimum-garden-perimeter-to-collect-enough-apples/description/

# https://docs.google.com/spreadsheets/d/17nRx3DHBUJ6KHa19W3amo6oej77eBpIM0HIwtGVV4ds/edit#gid=0
# Spent a LONG time in excel just trying to work out a formula. Got a cubic formula nobody else
# seems to be using.. FUCKING YES. Got the bisect version of it to work. Had to solve for
# ceil(4*x**3+6*x**2+2*x = 10**15) to get the upper bound


class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        # x = 1
        # while 4*x**3+6*x**2+2*x < neededApples:
        #     x += 1
        # return 8*x

        return 8 * bisect.bisect_left(
            range(62997), neededApples, key=lambda x: 4 * x**3 + 6 * x**2 + 2 * x
        )
