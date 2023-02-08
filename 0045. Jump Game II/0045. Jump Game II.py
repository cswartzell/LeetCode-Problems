# 02-07-2023 Leetcode 45. Jump Game II
# https://leetcode.com/problems/jump-game-ii/description/


class Solution:
    def jump(self, nums: List[int]) -> int:
        # 02-07-2023 Blind Redo
        # if len(nums) == 1:
        #     return 0

        last_i = len(nums) - 1
        prev_max_i_reachable = 0
        next_max_i_reachable = 0
        num_jumps = 0

        while last_i > next_max_i_reachable:
            num_jumps += 1
            temp = 0
            for i in range(prev_max_i_reachable, next_max_i_reachable + 1):
                temp = max(temp, i + nums[i])
            prev_max_i_reachable = next_max_i_reachable + 1
            next_max_i_reachable = temp

        return num_jumps

        # num_jumps = 0
        # target = len(nums) - 1

        # #Save what INDEX the ith index can jump to
        # for i in range(len(nums)):
        #     # nums[i] = max(target, i + nums[i])
        #     nums[i] += i

        # # curr_max = 0
        # prev_max = 0
        # curr_max = min(target, nums[0])

        # while prev_max < target:
        #     prev_max, curr_max = curr_max, max(nums[prev_max : min(curr_max + 1, target)])
        #     num_jumps += 1
        # return num_jumps

        # #ok... this works but is a little weird. Curr_pos is kind of a misnomer.
        # #Maybe just "prev_max" would have been better. We are looking, slice by slice,
        # #from the last max (initially this is [0:0+1], or JUST the starting index), to
        # #the new max reachable. It doesnt actually matter where we jumped to on the last
        # #hop. In fact we DONT want to check from there to the new max it could then reach as
        # #that is double checking over slice sections.
        # #so, lets take the input [2,3,1,1,4,0]. First we calculate the INDEX each element in
        # #the list can reach, which is just its index plust its value: [2,4,2,3,8, 5]
        # # We start on 0 and can hop to index 1 or 2. We then see how far EITHER of these
        # # could get us in the next hop. It doesnt matter which, nor do we need to land
        # # on index 1 as if we really made the jump. We sort of "collect" the next max
        # # by iterating over all the spaces in the current slice (implicitly, during the max())
        # # and know, while the target is out of reach, we may as well stay on the current
        # # position (prev_max) rather than going back to index with the larget NEXT jump. We could have
        # # jumped at least this far from the last collected jump, and so the NEXT max must
        # # be after this point. In our example, [2,4,2,3,8,5], we DONT set curr_pos to 1
        # # after the first jump, even though the value of nums[1] is higher than nums[2]
        # # We instead "collected" the idx4 jump while passing through, and know the NEXT
        # # highest index/jump must be between the end of the last jump, and curr_max

        # # num_jumps = 0
        # # curr_pos = len(nums) - 1

        # # #Save what INDEX the ith index can jump to
        # # for i in range(len(nums)):
        # #     nums[i] += i

        # # #Jumping backwards, find the furthest back (first element)
        # # #that could get to the current position, thus jumping backwards
        # # #the most each time. I think this is O(n**2) though so... real bad?
        # # while curr_pos != 0:
        # #     i = 0
        # #     while i < curr_pos:
        # #         if nums[i] >= curr_pos:
        # #             curr_pos = i
        # #             num_jumps += 1

        # # return num_jumps
