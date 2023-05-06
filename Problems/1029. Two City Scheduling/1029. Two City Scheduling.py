"""03-27-2022 LeetCode 1029. Two City Scheduling"""

from ast import List


class Solution:
    def twoCitySchedCost(self, costs) -> int:
        cost_dif = []
        for a, b in costs:
            cost_dif.append([abs(a - b), a, b])
        cost_dif.sort(reverse=True)

        a_candidates = 0
        b_candidates = 0
        total = 0
        half_n = len(costs) // 2

        for _, a, b in cost_dif:
            if (b <= a and b_candidates < half_n) or (a_candidates == half_n):
                total += b
                b_candidates += 1
            else:
                total += a
                a_candidates += 1

        return total


test = Solution()
print(test.twoCitySchedCost([[10, 20], [30, 200], [400, 50], [30, 20]]))
