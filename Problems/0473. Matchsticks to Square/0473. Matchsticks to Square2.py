# 03-12-2024 Leetcode  0473. Matchsticks to Square
# https://leetcode.com/problems/matchsticks-to-square/
# Time: 15 Mins Challenge: 6/10
# Almost didnt work. TLE, MEM, need to sort to fail fast


# ONLY 15 matchsticks. Backtracking DFS for sure right?
# Have to try them all

from functools import cache


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        
        sum_len = sum(matchsticks)
        if sum_len % 4 != 0:
            return False
        self.side = sum_len // 4

        matchsticks.sort()

        @cache
        def stickIt( L, T, R, B, match):
            if L > self.side or T > self.side or R > self.side or B > self.side:
                return False
            if match == -1:
                return True

            return any([stickIt(L + matchsticks[match], T, R, B, match-1),
            stickIt(L, T + matchsticks[match], R, B, match-1),
            stickIt(L, T, R + matchsticks[match], B, match-1),
            stickIt(L, T, R, B + matchsticks[match], match-1)])

        return stickIt(0, 0, 0, 0, len(matchsticks) - 1)



        # sum_len = sum(matchsticks)
        # if sum_len % 4 != 0:
        #     return False
        # self.side = sum_len // 4

        # matchsticks.sort()

        # @cache
        # def stickIt( L, T, R, B, match):
        #     if L > self.side or T > self.side or R > self.side or B > self.side:
        #         return False
        #     if match == -1:
        #         return True

        #     return any([stickIt(L + matchsticks[match], T, R, B, match-1),
        #     stickIt(L, T + matchsticks[match], R, B, match-1),
        #     stickIt(L, T, R + matchsticks[match], B, match-1),
        #     stickIt(L, T, R, B + matchsticks[match], match-1)])

        # return stickIt(0, 0, 0, 0, len(matchsticks) - 1)
