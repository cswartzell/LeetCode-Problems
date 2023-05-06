# 03-12-2023  2202. Maximize the Topmost Element After K Moves
# https://leetcode.com/problems/maximize-the-topmost-element-after-k-moves/description/

# I suspect DP. If k = 0 moves, the answer is the top of the pile[0]
# If k = 1 we MUST perform a move, and the only one is to pop, so pile[1]
# If k = 2 we again are forced into the first move. Then we can pop again,
# or put the first val back. max(pile[0], pile[2]). Pile(1) cannot be chosen
# If k = 3, make first pop, we can then pop again, and again to get to to pile[3]
# pop, pop push meanse max(pile[0], pile[1]), pop push pop means pile[1]. pile[2] cannot be chosen
# Pop push push is not allowed
# k = 4: pop pop pop pop: pile[4], pop pop pop push: max(piles[0,1,2]) NOT 3,
# pop pop push pop: pile[2], pop pop push push: pile[0],
# pop push pop pop: The first two cancel eachother out, so its just pop pop again, pile[2]
# pop push pop push: cancel, pile[0], pop push push pop: NOT ALLOWED, pop push push push: NA
# So it looks like its just max(nums[:k-1]+nums[k]): the max num in the first k nums
# EXLUDING the k-1th index

# except for the stupid case where we cannot perform enough actions. Is a list of len(1)
# the only time this is true? We must pop first, then ANY push would restore the pile to how it
# was. If there are two elements or more you can always end up with a non empty pile: after
# n EVEN number pop push pairs the pile will be how it was. After n ODD number pop (push pop)...
# pairs there will be only one missing num.

# So if len(nums) == 1 and k is odd, then the pile will be empty


# OK, pretty well reasoned... except I only accounted for k LESS than len(nums)
# If k is LARGER than len(nums) we have to do another even/odd test. We MUST
# perform k moves. Now I think we have to facor in the parity of len(nums) in the first place

# 4 cases:
# 1) len(nums) is even, k is even
# 2) len(nums) is even, k is odd
# 3) len(nums) is odd, k is even
# 3) len(nums) is odd, k is odd

# Nevermind, we have at least one extra operation, so we can always use that op to
# put the max(pile) on top.

# Now what about k = len(n) even and odd?
# We cannot leave an empty pile so they cannot all be pops, there must be at least one push
# so max(pile[:len(pile)]), we exclude the last element


class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        if k == 0:
            return nums[0]
        elif len(nums) == 1 and k & 1:
            return -1
        elif len(nums) > k:
            return max(nums[: k - 1] + [nums[k]])
        elif len(nums) == k:
            return max(nums[: k - 1])
        else:
            return max(nums)
