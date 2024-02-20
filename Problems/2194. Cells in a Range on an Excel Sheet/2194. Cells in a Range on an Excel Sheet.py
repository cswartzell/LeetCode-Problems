# 02-19-2024 Leetcode 2194. Cells in a range on an Excel Sheet



import typing
import string

class Solution:
    def cellsInRange(self, s: str) -> list[str]:
        L,R = 0, 0
        
        while s[R] in string.ascii_uppercase:
            R += 1
        col1 = s[L:R]
        L = R
        while s[R] != ":":
            R += 1
        row1 = int(s[L:R])
        R += 1
        L = R
        while s[R] in string.ascii_uppercase:
            R += 1
        col2 = s[L:R]
        row2 = int(s[R:])

        A = ord("A")
        ans = [col1+str(row1)]
        curr_row = row1
        curr_col = [ord(ltr)-A for ltr in col1]


        LAST = col2+str(row2)
        while ans[-1] != LAST:
            if curr_row < row2:
                curr_row += 1
            else:
                curr_row = row1
                idx = len(curr_col) - 1
                while idx >= 0 and curr_col[idx] == 25:
                    curr_col[idx] = 0
                    idx -= 1
                if idx == -1:
                    curr_col.append(0)
                else:
                    curr_col[idx] += 1
            
            ans.append("".join(chr(x+A) for x in curr_col)+str(curr_row))

        return ans
    
    
check_it = Solution()
print(check_it.cellsInRange("X3:AB5"))