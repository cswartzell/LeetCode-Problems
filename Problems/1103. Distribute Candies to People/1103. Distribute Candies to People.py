# 04-02-2023 Leetcode 1103. Distribute Candies to People
# https://leetcode.com/problems/distribute-candies-to-people/description/


class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        dist = int((math.sqrt(8 * candies + 1) - 1) / 2)
        rounds = dist // num_people

        ans = [
            (rounds - 1) * (rounds) * num_people // 2 + (i + 1) * rounds
            for i in range(num_people)
        ]
        remainder = candies - sum(ans)
        i, nxt = 0, rounds * num_people + 1
        while remainder > 0:
            ans[i] += min(remainder, nxt)
            remainder -= nxt
            i += 1
            nxt += 1
        # check = sum(ans)
        return ans
