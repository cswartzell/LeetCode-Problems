# 09-12-2023 Neetcode 128. Longest Consecutive Sequence
# https://leetcode.com/problems/longest-consecutive-sequence/
# Time: 75 Minutes

# Bucket sort? Oh no, 2* 10**9 buckets. Seems like a lot
# Maybe like a union-find?

# Upon seeing a number there are two possibilities:
# A) we have already seen it: move on
# B) She new

# If new, it MAY extend a sequence on the right, or the Left
# Use dicts. Look at num-1 and num + 1
# Maybe 2 dicts? run_starts_with_x and run_ends_with_x
# Check both dicts. X may BRIDGE two, and thus we have a more
# complicated scenario: delete starts_with x + 1, delete ends_with x - 1
# Can save JUST the length of the run, not the run itself right?

# from collections import defaultdict


# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         if len(nums) == 0:
#             return 0

#         ends_with = defaultdict(int)
#         starts_with = defaultdict(int)

#         max_sequence = 1

#         for num in nums:
#             #seen already
#             if num in ends_with:
#                 continue

#             if num - 1 in ends_with and num + 1 in starts_with:
#                 ends_with[num] = ends_with[num - 1]
#                 starts_with[num] = starts_with[num + 1]
#                 starts_with[ends_with[num - 1]] = starts_with[num + 1]
#                 ends_with[starts_with[num + 1]] = ends_with[num - 1]
#                 max_sequence = max(max_sequence, starts_with[num] - ends_with[num] + 1)
#             elif num - 1 in ends_with:
#                 ends_with[num] = ends_with[num - 1]
#                 starts_with[num] = num
#                 starts_with[ends_with[num]] = num
#                 max_sequence = max(max_sequence, num - ends_with[num] + 1)
#             elif num + 1 in starts_with:
#                 starts_with[num] = starts_with[num + 1]
#                 ends_with[num] = num
#                 ends_with[starts_with[num]] = num
#                 max_sequence = max(max_sequence, starts_with[num] - num + 1)
#             else:
#                 ends_with[num] = num
#                 starts_with[num] = num

#         return max_sequence
        
        
        
        # DID NOT TRY THIS DUMB BUCKET SORT WITH BIG OLE buckets
        # I first thought it was just 10**5, which is doable

        # bucket = [0 for _ in range(2*10**9 + 1)]
        # for num in nums:
        #     bucket[num + 10**9] = 1

        # max_consecutive = 0
        # curr_consecutive = 0
        # for i in range(2*10**9 + 1):
        #     if bucket[i] == 1:
        #         curr_consecutive += 1
        #     else:
        #         max_consecutive = max(max_consecutive, curr_consecutive)
        #         curr_consecutive = 0

        # return max_consecutive










# 5 possibilities:
# Seen it: Discard and continue
# Not adjacent to existing runs: Start a new run, adding to both dicts
# One before a given run: Delete that run from starts, append new num to run, add to starts
# One fter Ends, delete from Ends, Append, add new to ends
# LINKS two runs: Delete both. Link. Add to both



class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
            longest_streak = 0
            num_set = set(nums)

            while num_set:
                current_num = min(num_set)
                current_streak = 1
                remove_nums = {current_num}

                while current_num + 1 in num_set:
                    remove_nums.add(current_num + 1)
                    current_num += 1
                    current_streak += 1
                
                num_set = num_set.difference(remove_nums)
                longest_streak = max(longest_streak, current_streak)

            return longest_streak

 