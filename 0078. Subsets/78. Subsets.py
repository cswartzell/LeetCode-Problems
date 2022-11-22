"""02-13-2022 LeetCode 78. Subset"""
# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:

# nums = sorted(nums)
nums = [1, 2, 3]
power_set = [[]]  # nums has at least one element


# --------------------------The real answer: had to read solutions to understand. Darn, it's so obvious too

for num in nums:
    power_set += [sub_set + [num] for sub_set in power_set]
print(power_set)

# --------------------------------------Attempt #2 was much cleaner and readable. Surely I can combine some of these lines
# for num in nums:
#     for sub in range(len(power_set)):
#         temp_sub = list(power_set[sub])
#         temp_sub.append(num)
#         power_set.append(temp_sub)

# print(power_set)
# --------------------------------------

# OK, only somewhat proud of this. Obviously a bit of a pasta dish
# I was SO CLOSE to the right idea on bringing in one new digit and
# appending it to the exiting elements of the power_set for each
# num in nums. If I had just refactored the logic I basically had
# the above

# temp_list = []
# temp_list2 = []
# new_set = 0
# kstart = 0

# for i in range(1, len(nums)):
#     # Number elements in subset we're getting
#     old_set = new_set
#     new_set = len(power_set)
#     for j in range(old_set, len(power_set)):
#         # Index of starting element in powerset for each subset
#         temp_list = power_set[j].copy()
#         if temp_list != []:
#             kstart = nums.index(min(temp_list)) + 1
#         for k in range(kstart, len(nums)):
#             temp_list2 = temp_list.copy()
#             # Iterater for generating subset
#             if nums[k] not in temp_list2:
#                 temp_list2.append(nums[k])
#             if sorted(temp_list2) not in power_set and len(temp_list2) == i:
#                 power_set.append(sorted(temp_list2.copy()))
# power_set.append(nums)

# print(power_set)
