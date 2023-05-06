# 03-21-2023 Leetcode 2576. Find the Maximum Number of Marked Indices
# https://leetcode.com/problems/find-the-maximum-number-of-marked-indices/


class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        # nums.sort()
        # smol_bois = nums[:-1]
        # big_bois = nums[-1:]

        # marked = 0

        # # while True: may be enough?
        # while smol_bois and big_bois:
        #     curr_match = big_bois.pop()
        #     right_idx = bisect.bisect_right(smol_bois, (curr_match // 2)) - 1
        #     if right_idx == -1:
        #         break
        #     marked += 2
        #     big_bois = smol_bois[right_idx + 1:] + big_bois
        #     smol_bois = smol_bois[:right_idx]

        # return marked

        nums.sort(reverse=True)
        smol_bois = nums[-1:]
        big_bois = nums[:-1]
        marked = 0

        # while True: may be enough?
        while smol_bois and big_bois:
            curr_match = smol_bois.pop()
            right_idx = bisect.bisect_right(big_bois, curr_match * 2)
            if right_idx == len(big_bois):
                break
            marked += 2
            big_bois = big_bois[right_idx - 1 :]
            smol_bois = big_bois[:right_idx] + smol_bois

        return marked
