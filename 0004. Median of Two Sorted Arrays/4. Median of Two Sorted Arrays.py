from heapq import merge
from statistics import median

nums1 = [1, 2]
nums2 = [3]


print(median(merge(nums1, nums2)))

# merged = list(merge(nums1, nums2))
# if ((len(nums1) + len(nums2)) %2) == 0:
#     print((merged[int((len(nums1) + len(nums2)) /2) -1] + merged[int((len(nums1) + len(nums2)) /2)])/2)
# else:
#     print((merged[int((len(nums1) + len(nums2) -1) /2)]))


# abominable one liner thats not quite right? It works here and literally gives a different answer on leetcode WITH THE SAME INPUT?!
# Whatever, its overly clever and completely unreadable
# print((list(merge(nums1, nums2))[floor((len(nums1) + len(nums2) - 1) / 2)] + list(merge(nums1, nums2))[ceil((len(nums1) + len(nums2) - 1) / 2)])/ 2)
