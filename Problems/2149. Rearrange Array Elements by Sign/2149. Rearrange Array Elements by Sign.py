# 02-13-2024 Leetcode 2149. Rearrange Array Elements by Sign
# https://leetcode.com/problems/rearrange-array-elements-by-sign/?envType=daily-question&envId=2024-02-14
# Time: 15mins? Challenge: 3/10

# Weird Two Pointer
# If it was a linked list, it could be done in place in O(n)

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # pos = 0
        # neg = 0

        # ans = []

        # while len(ans) < len(nums):
        #     while nums[pos] < 0:
        #         pos += 1
        #     ans.append(nums[pos])
        #     pos += 1

        #     while nums[neg] > 0:
        #         neg += 1
        #     ans.append(nums[neg])
        #     neg += 1

        # return ans

        # In place for fun. Just need to arrange the positives in even idxs starting
        # at 0. Once done, the negs will automatically be in odd indexes and we dont
        # care about their ordering
        
        # 4 options: 
        # idx is even and num is positive: Do Nothing
        # idx is even and num is negative: swap the NEXT positive to here
        #     this step requires looking ahead
        # idx is odd and num is positive: swap with next negative
        #    this step requires looking ahead
        # idx is odd and num is negative: Do nothing


        # UNSURPRING< TLE
        # place = 0
        # while place < len(nums):            
        #     # idx is EVEN, as we are doing even/odd in order, repeating 
        #     # if num negative search ahead for the next positive by copying the
        #     # next values forward til we find it. Swap it into place
        #     # 
        #     if nums[place] < 0:
        #         next_num = place + 1
        #         temp = nums[place]
        #         while nums[next_num] < 0:
        #             temp, nums[next_num] = nums[next_num], temp
        #             next_num += 1
        #         nums[place], nums[next_num] = nums[next_num], temp
        #     place += 1

        #     # idx ODD, num positive
        #     if nums[place] > 0:
        #         next_num = place + 1
        #         temp = nums[place]
        #         while nums[next_num] > 0:
        #             temp, nums[next_num] = nums[next_num], temp
        #             next_num += 1
        #         nums[place], nums[next_num] = nums[next_num], temp
        #     place += 1

        # return nums


