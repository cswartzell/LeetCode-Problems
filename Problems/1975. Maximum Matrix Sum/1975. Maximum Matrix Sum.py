# 03-10-2023 1975. Maximum Matrix Sum
# https://leetcode.com/problems/maximum-matrix-sum/description/

# Ok, I legit love this one. Its just a logic puzzle:
# 0) We want to flip as many negatives to positive as possible, and for
# the negatives to remain we wan them to be of the smallest value
# 1) Any two negatives next to each can simply cancel and become positive
# 2 We DONT want to swtich two positives to negative, though we can always undo Its
# 3) Switching a negative and a positive causes the negative to "traval",
# and we can get a negative thus to inch its way around the board.
#  AS A RESULT, we can move negatives together and canel out their sign, from
# anywhere. Thus, We can easily cancel ALL the negatives if there are an even
# amount of them to start with: move them together and the pairs anihilate
# If there are an odd number of negatives to begin with then we can never
# get rid of the last one. We shoul have it be the number with the smallest
# magnitude. So: just sum the absolute values in array and maybe subtract the min


class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        neg_count = 0
        min_val = 10**5 + 1
        summed = 0
        for row in matrix:
            for ele in row:
                summed += abs(ele)
                min_val = min(min_val, abs(ele))
                neg_count += 1 if ele < 0 else 0

        return summed - 2 * min_val * (neg_count & 1)
