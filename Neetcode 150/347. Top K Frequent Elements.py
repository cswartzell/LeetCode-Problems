# 09-11-2023 Neetcode 347. Top K Frequent Elements
# https://leetcode.com/problems/top-k-frequent-elements/
# Time: 5 mins

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:   
            count_nums = collections.Counter(nums)
            k_most_frequent = []
            for val, freq in count_nums.items():
                if len(k_most_frequent) < k:
                    heapq.heappush(k_most_frequent, (freq, val))
                else:
                    if freq > k_most_frequent[0][0]:
                        heapq.heappushpop(k_most_frequent, (freq, val))

            return [val for _, val in k_most_frequent]



#I mean, there is literally a Counter method that just does this.
# class Solution:
    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:   
        # count =  collections.Counter(nums)
        # counted_tuples = []
        # for num in count.keys():
        #     # could do this as a heap for sorting as we go but meh
        #     counted_tuples.append((count[num], num))
        # counted_tuples.sort(reverse=True)
        # return [val for _, val in counted_tuples[:k]]