"""docstring goes here"""
from collections import Counter

nums = [0, 1]
new_sum = 0
prefix_sum = Counter()
prefix_sum[0] = -1
longest_contsub = 0


for i in range(len(nums)):
    new_sum += 1 if nums[i] else -1
    if new_sum not in prefix_sum:
        prefix_sum[new_sum] = i
    else:
        longest_contsub = max(longest_contsub, (i - prefix_sum[new_sum]))


print(longest_contsub)
# from collections import Counter

# nums = [0,1]
# new_sum = 0
# prefix_sum = Counter()
# prefix_sum[0] = 0
# longest_contsub = 0
# i = 0

# while i < len(nums):
#     new_sum += 1 if nums[i] else -1
#     i += 1
#     if new_sum not in prefix_sum:
#         prefix_sum[new_sum] = i
#     else:
#         longest_contsub = max(longest_contsub, (i - prefix_sum[new_sum]))


# print(longest_contsub)

# per usual, the following TECHNICALLY works, but times out. Unsurprsing as worst case is O(n!) Ouch
# the excuse is that it starts with the longest possible subarray, and checks downward, stopping
# when it finds the first qualifier, but that could be n steps

# from collections import Counter

# nums = [0,1,0,1,0,1,0,1]
# lnums = len(nums)
# longest_contsub = 0
# n = 0

# for i in range(lnums-1):
#     while n <= i:
#         curr_sub = Counter(nums[n:lnums-i+n])
#         if curr_sub.get(0) == curr_sub.get(1):
#             print(lnums-i)
#         n += 1
#     n = 0
