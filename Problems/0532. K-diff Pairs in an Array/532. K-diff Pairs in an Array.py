"""02-08-2022 LeetCode prolem 532"""
# from collections import OrderedDict

nums = [3, 1, 4, 1, 5]
k = 2

kdiffs = 0
kdiff_pairs = set()
nums_dict = dict()

for i in range(len(nums)):
    nums_dict.update({nums[i]: i})

for i in range(len(nums)):
    l = nums[i] - k
    m = nums[i] + k

    if l in nums_dict and nums_dict.get(l) > i and nums_dict.get(l) < len(nums):
        if (nums[i], nums[nums_dict.get(l)]) not in kdiff_pairs:
            kdiff_pairs.add((nums[i], nums[nums_dict.get(l)]))
            kdiff_pairs.add((nums[nums_dict.get(l)], nums[i]))
            kdiffs += 1
    if m in nums_dict and nums_dict.get(m) > i and nums_dict.get(m) < len(nums):
        if (nums[i], nums[nums_dict.get(m)]) not in kdiff_pairs:
            kdiff_pairs.add((nums[i], nums[nums_dict.get(m)]))
            kdiff_pairs.add((nums[nums_dict.get(m)], nums[i]))
            kdiffs += 1

# # return kdiffs
print(kdiffs)
