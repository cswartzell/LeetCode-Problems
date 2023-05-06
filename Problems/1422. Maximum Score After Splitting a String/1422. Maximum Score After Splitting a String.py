# 04-12-2023 Leetcode 1422. Maximum Score After Splitting a String
# https://leetcode.com/problems/maximum-score-after-splitting-a-string/description/

# Linear Scan X2?


class Solution:
    def maxScore(self, s: str) -> int:
        # Count 1s first
        # R_score = sum(one == "1" for one in s[1:])
        # L_score = 1 if s[0] == "0" else 0
        # max_score = L_score + R_score

        # for char in s[1:-1]:
        #     if char == "0":
        #         L_score += 1
        #     else: R_score -= 1
        #     max_score = max(max_score, L_score + R_score)
        # return max_score

        # score = sum(one == "1" for one in s[1:]) + int(s[0] == "0")
        # max_score = score
        # for char in s[1:-1]:
        #     if char == "0": score += 1
        #     else: score -= 1
        #     max_score = max(max_score, score)
        # return max_score

        # score =
        # max_score = score
        # for char in s[1:-1]:
        #     if char == "0": score += 1
        #     else: score -= 1
        #     max_score = max(max_score, score)
        # return max_score

        return max(
            itertools.accumulate(
                s[1:-1],
                lambda x, y: x + 1 if y == "0" else x - 1,
                initial=sum(one == "1" for one in s[1:]) + int(s[0] == "0"),
            )
        )
