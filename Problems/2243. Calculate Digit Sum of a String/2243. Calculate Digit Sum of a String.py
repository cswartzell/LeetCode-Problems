# 04-08-2023 Leetcode 2243. Calculate Digit Sum of a String
# https://leetcode.com/problems/calculate-digit-sum-of-a-string/description/


class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            s = "".join(
                str(sum(ord(char) - 48 for char in s[i * k : min((i + 1) * k, len(s))]))
                for i in range(math.ceil(len(s) / k))
            )
        return s

        # while len(s) > k:
        #     next_s = ""
        #     for i in range(math.ceil(len(s)/k)):
        #         slice_start = i*k
        #         slice_end = min((i+1)*k,len(s))
        #         len_k_slice = s[slice_start:slice_end]
        #         int_slice = [ord(char) - 48 for char in len_k_slice]
        #         slice_sum = sum(int_slice)
        #         str_slice_sum = str(slice_sum)
        #         next_s += str_slice_sum
        #     s = next_s
        # return s
