# 04-04-2023 Leetcode 1590. Make Sum Divisible by P
# https://leetcode.com/problems/make-sum-divisible-by-p/description/


# I think a prefix sum here will be helpful. 
# We couild do something like note the divors AT each index given the prefix sum at that point
# but that seems a bit much to do in prep.

#Ok, so we want to remove the LEAST amound of elements but can start anywhere and grow 
#out as a contiguous subarray. There is the obvious sliding window version, which would be o(n**2)

#To be clear if to_remove = sum(arr) % p, then we need sum(sub_array) % p == to_remove. 
#The sum of the subarray doesnt have to EQUAL the amount to remove, but be in the same
#residue class. 

#Ok... out of ideas. Sliding window it is. At least we can do a rolling sum so its not
#adding the whole window up each time (well, once its len 3 or more)

# class Solution:
#     def minSubarray(self, nums: List[int], p: int) -> int:
        # to_remove = sum(nums) % p

        # if to_remove == 0:
        #     return 0

        # for num in nums:
        #     if num % p == to_remove:
        #         return 1

        # #Darn. Longer sums

        # width = 2
        # while width < len(nums):
        #     L, R = 0, width
        #     curr_sum = sum(nums[L:R])
        #     if curr_sum % p == to_remove:
        #             return width
        #     while R < len(nums):
        #         curr_sum = curr_sum - nums[L] + nums[R]
        #         if curr_sum % p == to_remove:
        #             return width
        #         L += 1
        #         R += 1
        #     width += 1
        
        # return -1

        # target = sum(nums) % p
        # ans = math.inf
        # prefix = [0]
        # prefix_sum_at_idx = {0:0}
        # for i in  range(1, len(nums) + 1):
        #     prefix.append((prefix[-1] + nums[i-1]) % p)
        #     prefix_sum_at_idx[prefix[-1]] = i
        #     if prefix[-1] - target in prefix_sum_at_idx:
        #         ans = min(ans, i - prefix_sum_at_idx[prefix[-1] - target])

        # return ans if ans < len(nums) else -1

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        if sum(nums)%p==0:
            return 0
        target = sum(nums) % p
        dic,n = {0:-1},len(nums)
        cur,ret = 0,n
        for i,num in enumerate(nums):
            cur = (cur+num)%p
            if dic.get((cur-target)%p) is not None:
                ret = min(ret,i-dic.get((cur-target)%p))
            dic[cur] = i
        return ret if ret < n else -1