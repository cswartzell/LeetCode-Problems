#06-24-2023 Leetcode 689. Maximum Sum of 3 Non-Overlapping Subarrays
# https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/submissions/


# Three deep "take it or not"? Input len is only 2000
# O(n**3) solutions are usually... not good

# I can tighten things up a bit by not repeatedly doing the additon, just
# start by saving all sums of len k into a dict with index i being the key

# Lets try this naive way first and see what we learn
# Ok, without even running it I see how we can do better. 
# Lets say we have picked an i and j index and are looking for our l index
# Once weve found the max index for l, we loop and increase k by one. But if
# k != l we havent overtaken l, and l will STILL be the largest. No need to 
# search again. A 3 nested loop performs these searches over and over.

#So instead of a dict for summing, we need to do DP. Start summing from the end
# and keep track of "the index with the largest sum of len k after this index"
# I think this gets us down to O(n**2) anmd maybe that will have to do?
# Loop all i, loop all j, immediately return l?
# Heck, add a summing function for j + l and cache that to reduce even more


#aaaaaaand still TLE. Jeez. Well, I think Im stumped. I got it down to a cached
# O(n**2) DP and still think thats pretty good. Surprised it doesnt work really.

#BAH! So close. I even had an inkling of intuition. So precomputing for l "index
# of largest sum after and including this one, in lexicographical orderr" is great.
# Now just do the same for I. That way we only have to slide j, the middle array, and
# can instantly grab the best i and l. Brilliant. Only works for the case of 3 indecies
# but it gets it down to O(n).


class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        # ksum = {}
        # curr_sum = sum(nums[:k])
        # ksum[0] = curr_sum
        # for i in range(len(nums)-k) # +1?
        #     curr_sum -= nums[i]
        #     curr_sum += nums[i+k]
        #     ksum[i] = curr_sum
        
        # # max_sum = 0
        # ans = [2001,2001,2001]
        # for i in range(len(nums)-3*k):
        #     for j in range(i+k, len(nums)-2*k):
        #         for l in range(j+k,len(nums)-k):
        #             if ksum[i]+ksum[j]+ksum[l] >= max_sum:
        #                 #compare for lexicographical ordering
        #                 #Can i just use less than for lists? I think so?
        #                 #If not, do something. Make it a string and compare,
        #                 # or go verbose and check element by element and just do a plain math LTE
        #                 if [i,j,l] < ans:
        #                     ans = [i,j,l]

        # curr_sum = sum(nums[len(nums)-k:])
        # max_sum = curr_sum
        # max_L = [0 for _ in range(len(nums)-k+1)]
        # max_L[len(nums)-k] = len(nums)-k        
        # ksum = {len(nums)-k:curr_sum}
        
        # for i in range(len(nums)-k-1,-1,-1):
        #     curr_sum += nums[i]
        #     curr_sum -= nums[i+k]
        #     ksum[i] = curr_sum
        #     if curr_sum >= max_sum:
        #         max_L[i] = i
        #         max_sum = curr_sum
        #     else:
        #         max_L[i] = max_L[i+1]
        
        # @cache
        # def twosum(j) -> int:
        #     return ksum[j]+ksum[max_L[j+k]]

        # max_sum = 0
        # ans = [2001,2001,2001]
        # for i in range(len(nums)-3*k+1):
        #     for j in range(i+k, len(nums)-2*k+1):
                #By only checking FORWARD, we are advancing the indexes. If we come upon
                # a tie to the current max_sum, it will necessarily be less lexicographical
                # so we only need to check when the new max_sum exceeds the previous.
                # No lexicographical check needed.

                #We could FURTHER cache this as we are indeed performing some repeated 
                # ksum[j]+ksum[l] calculations here. We could go whole hog and do the same
                # sort of prefix best sum for the combination of j+l but im not sure that
                # actually reduces complexity, just moves it elsewhere. Caching is best?

                #Hmm. You cant cache a lambda?
        #         if ksum[i]+twosum(j) > max_sum:
        #                 ans = [i,j,max_L[j+k]]
        #                 max_sum = ksum[i]+twosum(j)
        # return ans 

        curr_sum = sum(nums[len(nums)-k:])
        max_sum = curr_sum
        max_L = [0 for _ in range(len(nums)-k+1)]
        max_L[len(nums)-k] = len(nums)-k        
        ksum = {len(nums)-k:curr_sum}
        
        for i in range(len(nums)-k-1,-1,-1):
            curr_sum += nums[i]
            curr_sum -= nums[i+k]
            ksum[i] = curr_sum
            if curr_sum >= max_sum:
                max_L[i] = i
                max_sum = curr_sum
            else:
                max_L[i] = max_L[i+1]
        
        #now do the same for i:
        max_I = [0 for _ in range(len(nums)-3*k+1)]
        max_I[0] = 0        
        max_sum = ksum[0]
        for i in range(1, len(nums)-3*k+1):
            if ksum[i] > max_sum:
                max_sum = ksum[i]
                max_I[i] = i
            else:
                max_I[i] = max_I[i-1]
        
        # @cache
        # def twosum(i,l) -> int:
        #     return ksum[i]+ksum[l]

        max_sum = 0
        ans = [2001,2001,2001]
        for j in range(k, len(nums)-2*k+1):
            curr_sum = ksum[max_I[j-k]]+ksum[j]+ksum[max_L[j+k]]
            if curr_sum > max_sum:
                    ans = [max_I[j-k],j,max_L[j+k]]
                    max_sum = curr_sum
        return ans 