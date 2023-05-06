class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        # all over the place for speeds, 10%, and 90%
        ans = [[1]]
        for i in range(1, numRows):
            ans += [
                [1]
                + [
                    ans[i - 1][j] + ans[i - 1][j + 1]
                    for j in range(len(ans[i - 1]) - 1)
                ]
                + [1]
            ]

        return ans


#         #Huh, concat is faster than appends, even though we have an extra var assigned here
#         ans = [[1]]
#         for i in range(1, numRows):
#             row = [1]
#             for j in range(len(ans[i-1])-1):
#                 row += [ans[i-1][j]+ans[i-1][j+1]]
#             ans += [row + [1]]

#         return ans


#         ans = [[1]]
#         for i in range(1, numRows):
#             ans += [[1]]
#             for j in range(len(ans[i-1])-1):
#                 ans[i].append(ans[i-1][j]+ans[i-1][j+1])
#             ans[i] += [1]

#         return ans
