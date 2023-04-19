# 04-17-2023 Leetcode 628. Maximum Product of Three Numbers
# https://leetcode.com/problems/maximum-product-of-three-numbers/description/

# Its literally just the three largest numbers IF positive;
# BUT ITS NOT JUST POSITIVES! This is why we need to read the prompts and think
# about edge cases to start. Maybe sketch a solution before jumping to code.
# If we HAVE to take 1 negative, we can reverse this by taking a SECOND negative.
# In which case we choose the SMALLEST. If we MUST and CAN only take one negative,
# it should be the largest (closest to 0).

# Cases:
# 3 positives: take 3 largest positives
# MUST take a neg, NO zero: take the smallest number in abs val, and two smallest pos
# MUST take a neg, CAN take zero: take 0, rest dont matter
# MUST take 2 negs: take two smallest negs, Largest positive
# MUST take 3 negs: take 3 largest negs, or zero if possible.


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # pos, neg, zero = [], [], []
        # for num in nums:
        #     if num > 0:
        #         pos.append(num)
        #     elif num < 0:
        #         neg.append(num)
        #     else:
        #         zero = True
        # pos.sort()
        # neg.sort()

        # ans = []
        # # 3 Positives: Good- Include 3 largest as a posibility
        # if len(pos) >= 3:
        #     ans.append(pos[-1]*pos[-2]*pos[-3])

        # # 2 Positives, 1 negative: Bad- ONLY if this is the only choice,
        # # which will only be true if there are ONLY one neg and 2 positives in the first place
        # # Mininmize the damage
        # if len(pos) == 2 and len(neg) == 1:
        #     ans.append(pos[0]*pos[1]*neg[-1])

        # # 2 Negatives, 1 positive: Good- Always check as may beat 3 positives
        # if len(neg) >= 2 and len(pos) >= 1:
        #     ans.append(pos[-1]*neg[0]*neg[1])

        # # 3 negatives: Bad- Only if there are NO positives to select from:
        # # Minimize Damage
        # if len(pos) == 0 and len(neg) >= 3:
        #     ans.append(neg[-1]*neg[-2]*neg[-3])

        # #Mitigates bad only choices for inputs that include a zero.
        # if zero:
        #     ans.append(0)

        # return max(ans)
        nums.sort()
        return max(nums[0] * nums[1] * nums[-1], nums[-3] * nums[-2] * nums[-1])
