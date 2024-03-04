# 03-03-2024 Leetcode 948. Bag of Tokens
# https://leetcode.com/problems/bag-of-tokens/?envType=daily-question&envId=2024-03-04
# Time: 20 Challenge: 4/10


# Wild. I like it. 
# Firstly, it leaves off an important bit of info: can you have negative score? Presumably no.

# I sense backtracking, dp, and bit masks. For a MEDIUM?! 1000 tokens is a LOT. 
# Maybe this is just a binary search problem. I feel like this is "killing monsters"
# but that was a hard and only had 16 monsters. There must be an easier decision.

# Oh, i think this is easy. Its maybe just sort and 2 pointer. We only gain or lose
# 1 score per play, so we "sell" the least amount of power for 1 score, and "by"
# the most amount of power for 1 score. 

# We start with a score of zero, so can ONLY sell. We gain one score and sell the 
# least amount of power. Move up the least_power pointer. Keep track of max score.
# Now we could use this score to buy the most amount of power, then continuously sell
# that power til we cant to gain score. Repeat



class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        max_score = 0
        curr_score = 0

        tokens.sort()
        least_pow, most_pow = 0, len(tokens) - 1

        curr_pow = power

        while least_pow <= most_pow and curr_score >= 0:
            while least_pow <= most_pow and curr_pow >= tokens[least_pow]:
                curr_pow -= tokens[least_pow]
                curr_score += 1
                least_pow += 1
            max_score = max(max_score, curr_score)
            if least_pow <= most_pow:
                curr_pow += tokens[most_pow]
                most_pow -= 1
                curr_score -= 1

        return max_score
             