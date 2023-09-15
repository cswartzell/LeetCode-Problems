# 11-14-2023 Neetcode 4. Median of Two Sorted Arrays
# https://leetcode.com/problems/median-of-two-sorted-arrays/
# Time: INFINTY: REWATCH AND MEMORIZE
class Solution:
    def findMedianSortedArrays(self, A: List[int], B: List[int]) -> float:
        AL, AR = 0, len(A) - 1
        n = len(A) + len(B)


        while AL < AR:
            AM = AL + (AR - AL)//2
            BM = n//2 - AM  - 2 # + 1?

            if A[AM] > B[BM+1]:
                AR = AM - 1
            else:
                AL = AM

        return min(A[AL + 1], B[n - AL + 1])if n & 1 else (A[AL + 1] + B[n - AL + 1]) / 2


# # middle of n1, middle of n2:
# # if the same, we are done REGARDLESS of even/odd
# # if n1 is less than n2, then the middle has to be to the RIGHT of n1
# # if n1 is more than n2*, then the middle is LEFT of n2


# class Solution:
#     def findMedianSortedArrays(self, A: List[int], B: List[int]) -> float:
#         na, nb = len(A), len(B)
#         n = na + nb
        
#         def solve(k, a_start, a_end, b_start, b_end):
#             # If the segment of on array is empty, it means we have passed all
#             # its element, just return the corresponding element in the other array.
#             if a_start > a_end: 
#                 return B[k - a_start]
#             if b_start > b_end: 
#                 return A[k - b_start]

#             # Get the middle indexes and middle values of A and B.
#             a_index, b_index = (a_start + a_end) // 2, (b_start + b_end) // 2
#             a_value, b_value = A[a_index], B[b_index]

#             # If k is in the right half of A + B, remove the larger right half.
#             if a_index + b_index < k:
#                 if a_value > b_value:
#                     return solve(k, a_start, a_end, b_index + 1, b_end)
#                 else:
#                     return solve(k, a_index + 1, a_end, b_start, b_end)
#             # Otherwise, remove the smaller left half. 
#             else:
#                 if a_value > b_value:
#                     return solve(k, a_start, a_index - 1, b_start, b_end)
#                 else:
#                     return solve(k, a_start, a_end, b_start, b_index - 1)
        
#         if n % 2:
#             return solve(n // 2, 0, na - 1, 0, nb - 1)
#         else:
#             return (solve(n // 2 - 1, 0, na - 1, 0, nb - 1) + solve(n // 2, 0, na - 1, 0, nb - 1)) / 2