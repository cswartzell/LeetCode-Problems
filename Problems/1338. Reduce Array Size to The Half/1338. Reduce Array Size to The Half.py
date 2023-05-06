# 04-04-2023 Leetcode 1338. Reduce Array Size to The Half
# https://leetcode.com/problems/reduce-array-size-to-the-half/description/

# Find the frequency map of elements, those are the values to
# fit into a 0/1 knapsack of size ceil(len(arr)//2)


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        # arr_count = collections.Counter(arr)
        # values = sorted(arr_count.values())
        # target = len(arr)//2

        # ans = 0
        # while target > 0:
        #     ans += 1
        #     target -= values.pop()

        # return ans
        # In Python, we can use the built-in Counter class.
        counts = collections.Counter(arr)
        max_value = max(counts.values())

        # Put the counts into buckets.
        buckets = [0] * (max_value + 1)

        for count in counts.values():
            buckets[count] += 1

        # Determine set_size.
        set_size = 0
        arr_numbers_to_remove = len(arr) // 2
        bucket = max_value
        while arr_numbers_to_remove > 0:
            max_needed_from_bucket = math.ceil(arr_numbers_to_remove / bucket)
            set_size_increase = min(buckets[bucket], max_needed_from_bucket)
            set_size += set_size_increase
            arr_numbers_to_remove -= set_size_increase * bucket
            bucket -= 1

        return set_size
