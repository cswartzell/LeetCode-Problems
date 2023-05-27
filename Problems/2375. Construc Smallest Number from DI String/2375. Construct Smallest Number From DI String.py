# 05-27-2023 Leetcode 2375. Construct Smallest Number From DI String
# https://leetcode.com/problems/construct-smallest-number-from-di-string/description/

#Sort nums.
# We want to use the smallest possible numbers first as they are more significant
# build from Left to Right
# If "I", append the smallest num, followed by the next smallest: nums[0], nums[1]
# If "D", append the second smallest num, followed by the smallest: nums[1], nums[0]
# Oh, if we reverse sort the list we could just pop them

#Wait, no: there can be multiple D in a row, we need to process them all. 
#Ok, so instead if its an I, pop and append, thus the smallest number.
#WHILE its D, start a mini list: pop and append to that. 
#When at the end of the D series, reverse this list and simply add it:
#NOTE we need len d-series PLUS ONE in our mini list IF its followed by an i?
# If its not, we can truncate the list by one?
# So IIDDDI would be: add 1, 2. Start mini list [3,4,5,6], reverse and att it 1,2,6,5,4,3

#We need to consume the I following a D series by adding it to the mini list. OR it consumes
# and adds the final char of the string, the n+1 char

# Could do the above while nums.len > 1, then see if we need to switch the final position? 
# Oh! If there are any final bits, it will just be nums. Just add nums at the string buiilder
# step to either add the remainder digit, OR none. 

# Store built up ans as an list, return string builder

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        ans = []
        nums = ['9', '8', '7', '6', '5', '4', '3', '2', '1'][8-len(pattern):10]
        i = 0

        while i < len(pattern):
            if pattern[i] == "I":
                ans.append(nums.pop()) 
            else:
                deez = [nums.pop()] # Consume trailing I or final char AFTER D run
                while i < len(pattern) and pattern[i] == "D":
                    deez.append(nums.pop())
                    i += 1
                ans += deez[::-1]
            i += 1

        return "".join(ans+nums)

