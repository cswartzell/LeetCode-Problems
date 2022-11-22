"""5-09-2022 Leetcode 17. Letter Combinations of a Phone Number"""

# Hey look, its the basis for kakuro.
# Also, they list an n of up to 60, but it couldnt be more than 45
# Jeez... where to start. I could just make every combination (formal)
# using itertools combination... This is actually a good and clever, though
# language specific method.

# import itertools


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # return [list(x) for x in list(itertools.combinations({1,2,3,4,5,6,7,8,9}, k)) if sum(x) == n]
        digits = {1, 2, 3, 4, 5, 6, 7, 8, 9}
        combinations = itertools.combinations(digits, k)
        combinations = list(combinations)
        answer = []
        for x in combinations:
            if sum(x) == n:
                answer.append(x)
        return answer
