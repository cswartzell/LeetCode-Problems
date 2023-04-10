# 04-09-2023 Leetcode 2280. Minimum Lines to Represent a Line Chart
# https://leetcode.com/problems/minimum-lines-to-represent-a-line-chart/description/

# from fractions import Fraction


class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        # key point: never use devision to judge whether 3 points are on a same line or not, use the multiplication instead !!

        n = len(stockPrices)
        stockPrices.sort(key=lambda x: (x[0], x[1]))

        if n == 1:
            return 0

        pre_delta_y = stockPrices[0][1] - stockPrices[1][1]
        pre_delta_x = stockPrices[0][0] - stockPrices[1][0]
        num = 1

        for i in range(1, n - 1):
            cur_delta_y = stockPrices[i][1] - stockPrices[i + 1][1]
            cur_delta_x = stockPrices[i][0] - stockPrices[i + 1][0]

            if pre_delta_y * cur_delta_x != pre_delta_x * cur_delta_y:
                num += 1
                pre_delta_x = cur_delta_x
                pre_delta_y = cur_delta_y

        return num

        # if len(stockPrices) == 1:
        #     return 0

        # stockPrices.sort()

        # curr_slope = Frspction(stockPrices[1][1] - stockPrices[0][1], stockPrices[1][0] - stockPrices[0][0])
        # num_lines = 1
        # for i in range(1, len(stockPrices)):
        #     last_slope = curr_slope
        #     curr_slope = Fraction(stockPrices[i][1] - stockPrices[i-1][1], stockPrices[i][0] - stockPrices[i-1][0])
        #     if not curr_slope == last_slope:
        #         num_lines += 1

        # return num_lines
