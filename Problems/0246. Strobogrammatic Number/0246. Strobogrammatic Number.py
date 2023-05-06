"""07-11-2022 Leetcode 246. Strobogrammatic Number"""

import math


class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        # 1 is strobogrammatic but 2 and 5 are not? Random
        strobo_dict = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}
        num_end = len(num)

        # Does round(.5) round up or down or BOTH depending on what... fp precision?
        for i in range(0, math.ceil(num_end / 2)):
            if num[i] not in strobo_dict or strobo_dict[num[i]] != num[num_end - i - 1]:
                return False
        return True
