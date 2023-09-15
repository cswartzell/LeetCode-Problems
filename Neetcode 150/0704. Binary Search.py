# 11-13-2023 Neetcode 704. Binary Search
# https://leetcode.com/problems/binary-search/
# Time: 5 mins

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return i if 0 <= (i := bisect.bisect_left(nums, target)) < len(nums) and nums[i] == target else -1
        L, R = 0, len(nums) - 1

        while L < R:
            M = L + (R-L)//2
            if nums[M] > target:
                R = R - 1
            if nums[M] < target:
                L = M
            if nums[M] == target:
                return M

        return -1

# # 03-30-2023 Leetcode 704. Binary Search
# # https://leetcode.com/problems/binary-search/description/

# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         # return ans if 0 <= (ans := bisect.bisect_left(nums, target)) < len(nums) and nums[ans] == target else -1
#         # L, R = 0, len(nums) - 1

#         # while L <= R:
#         #     M = L + (R-L) // 2
#         #     if nums[M] < target:
#         #         L = M + 1
#         #     elif nums[M] > target:
#         #         R = M - 1
#         #     elif nums[M] == target:
#         #         return M
#         # return -1
        