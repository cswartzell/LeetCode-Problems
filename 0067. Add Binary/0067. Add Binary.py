# 12-09-2022 Leetcode 67. Add Binary
# https://leetcode.com/problems/add-binary/description/


# Lets not just use built in convert. TOO easy.
# reverse strings at first to simplify indexing?

# Well that was an exercize in stupidity. PAINFULLY obtuse
# Still, "I DID it", doing binary addition using only strings
# instead of any form of math. Now lets go see how to do it
# in like 4 lines


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = a[::-1]
        b = b[::-1]
        c = ""
        carry = False
        i = 0
        while i < min(len(a), len(b)):
            if carry:
                if a[i] == "1" and b[i] == "1":
                    c += "1"
                    carry = True
                elif a[i] == "1" or b[i] == "1":
                    c += "0"
                    carry = True
                else:
                    c += "1"
                    carry = False
            elif a[i] == "1" and b[i] == "1":
                c += "0"
                carry = True
            elif a[i] == "1" or b[i] == "1":
                c += "1"
            else:
                c += "0"
            i += 1

        if len(a) > len(b):
            while carry and i < len(a):
                if a[i] == "1":
                    c += "0"
                else:
                    c += "1"
                    carry = False
                i += 1
        elif len(b) > len(a):
            while carry and i < len(b):
                if b[i] == "1":
                    c += "0"
                else:
                    c += "1"
                    carry = False
                i += 1
        if carry:
            c += "1"
        c += a[i:] + b[i:]
        return c[::-1]
