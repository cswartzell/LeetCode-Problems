from collections import Counter
import collections

nums1 = [1]
nums2 = [-1]
nums3 = [0]
nums4 = [1]

# ok, so a combination of my excel spreadsheet idea of muxing two lists simulatneously, then muxing those two lists
# AND using a dict to make it faster?

n = len(nums1)
num_nil_sum = 0

# dnums1 = collections.Counter(nums1)
# dnums2 = collections.Counter(nums2)
# dnums3 = collections.Counter(nums3)
# dnums4 = collections.Counter(nums4)
iinj = collections.Counter()

for i in range(n):
    for j in range(n):
        iinj.update([nums1[i] + nums2[j]])

for k in range(n):
    for l in range(n):
        num_nil_sum += iinj[-(nums3[k] + nums4[l])]

print(num_nil_sum)

# #not positive that theres not a way to avoid a 4 level deep loop, but we can COUNT the items into a dictionary
# #and multiply by the number of occurances in a given list when its part of a zero sum.
# #may cut down on ops if there a lot of duplicates, but is still crap answer as the data space is MAX_INT


# n = len(nums1)
# num_nil_sum = 0

# dnums1 = collections.Counter(nums1)
# dnums2 = collections.Counter(nums2)
# dnums3 = collections.Counter(nums3)
# dnums4 = collections.Counter(nums4)

# for i in dnums1:
#     for j in dnums2:
#         for k in dnums3:
#             for l in dnums4:
#                 if i + j + k + l == 0:
#                     print(dnums1[i], " ", dnums2[j], " ", dnums3[k], " ", dnums4[l])
#                     num_nil_sum += dnums1[i] * dnums2[j] * dnums3[k] * dnums4[l]
# print(num_nil_sum)


# #obvious, naive O(n**4) solution. Obviously a problem

# for i in range(n):
#     for j in range(n):
#         for k in range(n):
#             for l in range(n):
#                 if nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0:
#                     num_nil_sum += 1
# print(num_nil_sum)
