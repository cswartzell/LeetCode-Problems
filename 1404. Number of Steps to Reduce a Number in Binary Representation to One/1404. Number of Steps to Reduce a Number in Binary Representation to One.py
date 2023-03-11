# 03-10-2023 Leetcode 1404. Number of Steps to Reduce a Number in Binary Representation to One
# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/description/


# If not math, we can def DP it

# its length of string and num zeros somehow. Or like two chars.

# "0" = N/A
# "1" = 0
# "10" = N/A = 1 10-1
# "11" = 3       11-100-10-1
# "100" = N/A
# "101" = 5      101-110-11-100-10-1
# "110" = N/A
# "111" = 4      111-1000-100-10-1
# "1000" = N/A
# "1001" = 7     1001-1010-101-110-11-100-10-1
# "1010" = N/A
# "1011" = 6     1011-1100-110-11-100-10-1
# "1100" = N/A
# "1101" = 6     1101-1110-111-1000-100-10-1
# "1110" = N/A
# "1111" = 5     1111-10000-1000-100-10-1
# "10000" = 4
# "10001" = 8    10001-10010-1101-1110-111-1000-100-10-1

# ...
# "1101" = 4

# Ok. I dont see a pattern, so I am going to have to go DP. I can use the existing computed info to pretty quickly
# cut down on the amount of time spent calculating. I am mad, surely there is just a math answer


class Solution:
    def numSteps(self, s) -> int:
        # return len(s) - 1 + collections.Counter(s)["0"]
        s = list(s)[::-1]
        num_steps = 0
        carry = False
        while s != ["1"]:
            num_steps += 1
            if s[0] == "0":
                s = s[1:]
                continue
            carry = True
            i = 1
            s[0] = "0"
            while i < len(s):
                if s[i] == "1":
                    s[i] = "0"
                    i += 1
                else:
                    s[i] = "1"
                    carry = False
                    break
            if carry:
                s.append("1")

        return num_steps
