# 11-14-2023 Neetcode 33. Search in Rotated Sorted Array
# https://leetcode.com/problems/search-in-rotated-sorted-array/
# Time: 15 mins

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        L, R = 0, len(nums) - 1
        rotated_start = -1
        while R >= L:
            M = L + (R - L)// 2
            if nums[M] > nums[M + 1]:
                rotated_start = M + 1
                break
            if nums[M - 1] > nums[M]:
                rotated_start = M
                break
            if nums[M] > nums[0]:
                L = M + 1
            else:
                R = M - 1

        if nums[rotated_start] <= target <= nums[len(nums) - 1]:
            L, R = rotated_start, len(nums) - 1    
        else:
            L, R = 0, rotated_start
        
        while L < R:
            M = L + (R - L)//2
            if target < nums[M]:
                R = M - 1
            elif target > nums[M]:
                L = M
        
        return nums[L] == target




# # So we cant even search through to find the pivot point?
# # Clearly a binary search with a twist... but what?
# # I guess we can binary search for the pivot, then
# # binary search again for the target
# # But what to search for initially? Its not 0...n, it could be anything

# # if we look at anyu two adjacent nodes there are only two possibilities:
# # either they are ascending and we have no clue if the split is left or right
# # or we found the pivot. What do we do if we have no clue?

# # Ok, i think im on to something. look at the two ends, and the middle value.
# # Now if it goes L < M < R we know its NOT rotated, L < M (implied) and M > R we know 
# # the rotation happens AFTER M (can be immediate) or vice versa:
# # if L > M (and thus M < R, may not need to check) then the rotate is LEFT of
# # middle. We can bsearch for the rotation point.


# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         L, R = 0, len(nums) - 1
        
#         while L <= R:        
#             M = L + (R - L) // 2
#             if nums[M] >= nums[-1]:
#                 L = M + 1 
#             else:
#                 R = M - 1
            
#         second_section_start  = min(L, len(nums)-1)
#         if second_section_start == 0:
#             second_section_start = len(nums)

#         if target >= nums[0] and target <= nums[second_section_start - 1]:
#             found = bisect.bisect_left(nums[:second_section_start], target)
#             return found if nums[found] == target  else -1
#         elif second_section_start < len(nums) and target >= nums[second_section_start] and target <= nums[-1]:
#             found = bisect.bisect_left(nums[second_section_start:], target)
#             return found + second_section_start if nums[found + second_section_start]  == target  else -1
#         else: 
#             return -1