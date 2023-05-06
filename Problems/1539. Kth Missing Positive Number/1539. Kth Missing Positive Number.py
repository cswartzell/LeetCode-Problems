# 03-05-2023 Leetcode 1539. Kth Missing Positive Number
# https://leetcode.com/problems/kth-missing-positive-number/description/

#Ugh I hate it. BRUTISH brute force for sure. Ugly. 

#Now on to the harder version... what the hell. There is kind of a prefix
#sum version using the triangular numbers but thats... tough

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        if k > arr[-1] - len(arr):
            return  len(arr) + k

        missing = 0
        last = arr[-1]
        i = 0
        should_be = 1
        while i < len(arr):
            next_num = arr[i]
            while next_num != should_be:
                missing += 1
                if missing == k:
                    return should_be
                should_be += 1
            i += 1
            should_be += 1