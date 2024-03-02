# 03-01-2024 Leetcode 2864. Maximum Odd Binary Number
# https://leetcode.com/problems/maximum-odd-binary-number/?envType=daily-question&envId=2024-03-01
# Time: 10 Challenge: 2

# Count the number of 1's an zeros
# The maximum odd binary is formed Right to Left:
# start with a 1 in the 2^0 bit to guarentee its odd, then add 
# ALL the zeros, then all remaining 1s. 

# We are guarenteed to have at least one 1 so we can naively proceed

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        # bits = collections.Counter(s)
        # ans = ["1"] + (["0"] * bits["0"] ) + (["1"] * max(bits["1"] - 1, 0))  
        # return "".join(reversed(ans))

        # return "".join(reversed(["1"] + ["0"]*s.count("0") + ["1"]*(s.count("1") - 1)))

        # i, o = [], []
        # for bit in s:
        #     if bit == "0":
        #         o.append("0")
        #     else:
        #         i.append("1")
        # i.pop()

        # return "".join(i + o + ["1"]) 

        return "".join(sorted(s, reverse=True)[1:] + ["1"])