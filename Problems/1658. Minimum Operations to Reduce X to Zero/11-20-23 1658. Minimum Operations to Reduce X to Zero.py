# 11-20-2023 Leetcode 1658. Minimum Operations to Reduce X to Zero
# https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/?envType=daily-question&envId=2023-09-20
# Time; 15mins


#So len(nums) is 10^5 which ought to preclude a recursive solution but 

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        # def reduce_it( x, num_steps, l, r) -> int:
        #     if x == 0:
        #         return num_steps
        #     elif l > r or x < 0:
        #         return 10**5 + 1
        #     return min( reduce_it( x - nums[l], num_steps + 1, l + 1, r), reduce_it( x - nums[r], num_steps + 1, l, r - 1))

        # ans = reduce_it( x, 0, 0, len(nums) - 1)
        
        # return ans if ans != 10**5 + 1 else -1

        L, R = 0, len(nums) - 1
        total = 0
        min_steps = math.inf

        while L < len(nums) and total < x:
            total += nums[L]
            # if total == 0:
            #     min_steps = min(min_steps, L + len(nums)-1-R)
            L += 1
        L -= 1
        if total == x:
            min_steps = min(min_steps, L + len(nums)-R)

        if total < x:
            return -1

        while L >= 0:
            total -= nums[L]
            L -= 1
            
            while total + nums[R] <= x:
                total += nums[R]
                R -= 1

            if total == x:
                min_steps = min(min_steps, L + len(nums)-R)
        
        return min_steps if min_steps != math.inf else -1