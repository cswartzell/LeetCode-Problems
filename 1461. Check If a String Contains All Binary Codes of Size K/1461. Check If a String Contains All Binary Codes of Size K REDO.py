# 03-13-2023 Leetcode 1461. Check If a String Contains All Binary Codes of Size K
# https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/description/


# 2^20 is just over a million, so not unreasonable to store a dict


class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        # bin_nums = set()
        # start, end = 0, k
        # # while end <= len(s):
        # while start <= len(s) - k:
        #     # if s[start:end] not in bin_nums:
        #     bin_nums.add(s[start:start+k])
        #     start += 1
        #     # end += 1

        # return len(bin_nums) ==  2**k

        return len(set(s[i : i + k] for i in range(0, len(s) - k + 1))) == 2**k
