# There is surely math trickery involved here and I'm not seing it.
# Firstly, I think there has to be an odd numbered len list, else there
# is an even number of XORings which should cancel right? [2, 1] and [3,5]
# means you get two copies of 2 ([2,3] and [2,5]) and so they XOR in and out.
# Same is true of all other numbers here, so the result is always 0.
# If you have an ODD number for both? I think you include them all. Also, it doesnt
# say the nums are unique, so we cant go by just len of list. You have to count the number
# of nums in each list, then multiply that by the len of the OTHER list. Add the counts from
# BOTH lists. Then any that have even counts get negated. Those with odd counts, XOR exactly 
# once?

# Wait... I think I'm double counting but also weirdly it doesnt matter that I am

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        counts = collections.Counter()

        for num in nums1:
           counts[num] += len(nums2) 
        for num in nums2:
           counts[num] += len(nums1)
        
        ans = 0
        for num, count in counts.items():
            if count % 2 == 1:
                ans ^= num

        return ans
