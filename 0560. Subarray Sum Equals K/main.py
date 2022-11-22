"""02-09-2022 LeetCode 560. Subarray Sum Equals K"""
from typing import Counter

nums = [2, 2, 2, 2, 2, 3, 4, 5, -2, 6, -5, -1, 7, -17]
k = 10
#nums = [1]
#k = 1

ksums = 0
numsums = Counter()

numsums[0] += 1
# if nums[0] == k:
#     ksums += 1
# if k == 0:
#     numsums.pop(0)

next_sum = 0

for i in range(len(nums)):
    next_sum += nums[i]
    if next_sum - k in numsums:
        ksums += numsums[next_sum - k]
    numsums[next_sum] += 1

print(ksums)

# for i in range(1, len(nums) + 1):
#     numsums.append(numsums[i - 1] + nums[i - 1])

# if k == 0:
#     numsums.pop(0)
# forward_numsums = Counter(numsums)

# for j in range(len(numsums)):
#     target = numsums[j] + k
#     ksums+= forward_numsums[numsums[j] + k]
#     forward_numsums[numsums[j] + k] = 0

# print(ksums)
