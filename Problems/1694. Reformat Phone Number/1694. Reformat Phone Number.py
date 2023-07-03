# 06-22-2023 Leetcode 1694. Reformat Phone Number
# https://leetcode.com/problems/reformat-phone-number/description/

class Solution:
    def reformatNumber(self, number: str) -> str:
        temp = []
        last_group = 0

        for i in range(len(number)):
            if number[i] != ' ' and number[i] != '-':
                temp.append(number[i])
                last_group += 1
            if last_group == 3:
                last_group = 0
                temp.append('-')
            

        if last_group == 0:
            return "".join(temp[:len(temp)-1])
        
        elif last_group == 1:
            temp[-3], temp[-2] = temp[-2], temp[-3]
        
        return "".join(temp)
        