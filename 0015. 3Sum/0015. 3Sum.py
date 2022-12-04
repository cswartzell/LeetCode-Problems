# 12-1-2022 Leetcode 15. 3Sum
# https://leetcode.com/problems/3sum/description/

# There are 3000*2999*2998=26,973,006,000 potential
# combinations of our input, so obviously brute force
# is right out. There is howver no need to calculate adding
# a third element, we COULD just store every sum of TWO elements
# and (using a hashmap) see if the the negative  is in our original
# nums. This is still a lot of calculating, 3000*2999 but 'only'
# 8,997,000. If I had to guess, thats perhasp STILL too large
# nut nothing else comes to mind right now. The space for nums[i]
# itself is rather large (-10**5 thur 10**5) so while we COULD
# start with say a Counter set to reduce the number of combinations
# and then multiply by said count value for succesful combinations...
# why? It would reduce average time, but not worst case

# Very poorly worded. "Notice the solution doesnt contain duplicates"
# seems to imply this follows from the rules, but it doesnt. It should
# be listed as an additional rule

from collections import Counter


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res, dups = set(), set()
        seen = {}
        for i, val1 in enumerate(nums):
            if val1 not in dups:
                dups.add(val1)
                for j, val2 in enumerate(nums[i + 1 :]):
                    complement = -val1 - val2
                    if complement in seen and seen[complement] == i:
                        res.add(tuple(sorted((val1, val2, complement))))
                    seen[val2] = i
        return res


# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         res = []
#         nums.sort()
#         for i in range(len(nums)):
#             if nums[i] > 0:
#                 break
#             if i == 0 or nums[i - 1] != nums[i]:
#                 self.twoSum(nums, i, res)
#         return res

#     def twoSum(self, nums: List[int], i: int, res: List[List[int]]):
#         seen = set()
#         j = i + 1
#         while j < len(nums):
#             complement = -nums[i] - nums[j]
#             if complement in seen:
#                 res.append([nums[i], nums[j], complement])
#                 while j + 1 < len(nums) and nums[j] == nums[j + 1]:
#                     j += 1
#             seen.add(nums[j])
#             j += 1


# #this is a pretty straight forward O(n**2) solution and still TLE?
# sorted_nums = sorted(nums)
# ans = set()
# for i in range(len(sorted_nums)-1):
#     #i will always be the lowest value in a triplet, so if i is positive
#     #then all 3 are and the sum cannot be zero
#     #Furthermore, we can skip duplicates of i
#     if (nums[i] > 0 or nums[i] == nums[i-1]) and i != 0:
#         continue
#     j, k = i + 1, len(sorted_nums) - 1
#     while j != k:
#         sumd = (sorted_nums[i] + sorted_nums[j] + sorted_nums[k])
#         if sumd < 0:
#             j += 1
#         elif sumd > 0:
#             k -= 1
#         elif sumd == 0:
#             ans.add((sorted_nums[i], sorted_nums[j], sorted_nums[k]))
#             k -= 1

# return ans


# ans = set()
# # seen_pairs = []
# nums_c = Counter(nums)
# nums_c_list = list(nums_c.keys())

# for i in range(len(nums_c.keys())):
#     for j in range(i,len(nums_c.keys())):
#         li, lj, lk = nums_c_list[i], nums_c_list[j], -(nums_c_list[i]+nums_c_list[j])
#         if -(nums_c_list[i] + nums_c_list[j]) in nums_c_list:
#             if tuple(sorted( (nums_c_list[i], nums_c_list[j], -(nums_c_list[i]+nums_c_list[j])) )) not in ans:
#                 # if nums_c_list[i] == nums_c_list[j] == 0 and nums_c[0] < 3 or \
#                 # nums_c_list[i] == -(nums_c_list[i]+nums_c_list[j]) and nums_c[nums[i]] < 2 or \
#                 # nums_c_list[j] == -(nums_c_list[i]+nums_c_list[j]) and nums_c[nums[j]] < 2 or \
#                 # nums_c_list[i] == nums_c_list[j] and nums_c[nums[i]] < 2 :
#                 #     continue
#                 if nums_c_list[i] == nums_c_list[j] == 0 and nums_c[0] < 3:
#                     continue
#                 if nums_c_list[i] == -(nums_c_list[i]+nums_c_list[j]) and nums_c[nums_c_list[i]] < 2:
#                     continue
#                 if nums_c_list[j] == -(nums_c_list[i]+nums_c_list[j]) and nums_c[nums_c_list[j]] < 2:
#                     continue
#                 if nums_c_list[i] == nums_c_list[j] and nums_c[nums_c_list[i]] < 2:
#                     continue
#                 ans.add(tuple(sorted( (nums_c_list[i],nums_c_list[j],-(nums_c_list[i]+nums_c_list[j])) )))
# return list(ans)
