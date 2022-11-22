"""03-27-2022 LeetCode 1337. The K Weakest Rows in a Matrix"""


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        #         row_str = []
        #         for x in range(len(mat)):
        #             row_str.append( (sum(mat[x]), x) )
        #         row_str.sort()
        #         weakest = []
        #         for i in range(k):
        #             weakest.append(row_str[i][1])
        #         return weakest

        # Build a list of (strength, index) pairs.
        strengths = [(sum(row), i) for i, row in enumerate(mat)]

        # Sort.
        strengths.sort()

        # Pull out and return the indexes of the first k entries.
        return [i[1] for i in strengths[:k]]
