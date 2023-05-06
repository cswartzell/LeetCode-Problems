# 02-19-2023 LeetCode 35. Search Insert Position
# https://leetcode.com/problems/search-insert-position/description/

# DO A BINARY SEARCH
# When down to two elements, if neither is the target, then
# the target index SHOULD be between them, ie should be the index
# of the larger value


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # 02-19-2023 blind redo
        # Asking for search O(nlogn) on a sorted list. Yep, Bsearch
        if target < nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)

        l, r = 0, len(nums) - 1
        while l < r:
            mid = (
                l + r
            ) // 2  # No, we dont have to do the subtraction trick to avoid overflow, but "l + (r-l)/2" so I remember it
            if nums[mid] > target:
                r = mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                return mid
        return r

        # # if target < nums[0]:
        # #     return 0
        # # if target > nums[-1]:
        # #     return len(nums)

        # # l = 0
        # # r = len(nums) - 1
        # # # mid = (l+r)//2

        # # while l < r:
        # #     mid = (l+r)//2
        # #     if target > nums[mid] and l != mid:
        # #         l = mid
        # #     elif target < nums[mid] and r != mid:
        # #         r = mid
        # #     elif nums[l] == target:
        # #         return l
        # #     elif nums[mid] == target:
        # #         return mid
        # #     else:
        # #         return r

        # # return r

        # #As suspected, I have the clunky version. I can never remember the offsets,
        # #even though its easy. We are using the mid/pivot to compare, so if its less
        # #then we can move the right pointer BEYOND the pivot to the left. If the pivot
        # #is smaller than the target, we can move the left pointer BEYOND the pivot.
        # #If it IS the pivot, simply return.
        # #The tricky bit is remembering that L CAN == R, (thus while L <= R)
        # #So we check the worst case, binary searching all the way. I would have assumed
        # #the intended index if unfound would be R, but its L in this case. Off by One errors
        # #are a common theme for Binary Search.

        # #https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/solutions/769698/Python-Clear-explanation-Powerful-Ultimate-Binary-Search-Template.-Solved-many-problems
        # #is a template to help remember Binary Search Parameters.
        # left, right = 0, len(nums) - 1
        # while left <= right:
        #     pivot = (left + right) // 2
        #     if nums[pivot] == target:
        #         return pivot
        #     if target < nums[pivot]:
        #         right = pivot - 1
        #     else:
        #         left = pivot + 1
        # return left
