# 03-11-2024 Leetcode 791. Custom Sort String
# https://leetcode.com/problems/custom-sort-string/description/?envType=daily-question&envId=2024-03-11
# Time: 20 Challenge: 2/10

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # s_count = collections.Counter(s)
        # s_builder = []
        # for char in order:
        #     s_builder += [char] * s_count.pop(char,0)
        # for char in s_count:
        #     s_builder += [char] * s_count[char]
            
        # return "".join(s_builder)

        s_count = collections.Counter(s)
        s_builder = []
        for char in order:
            s_builder += [char] * s_count[char]
            del s_count[char]
        for char in s_count:
            s_builder += [char] * s_count[char]
            
        return "".join(s_builder)

        # s_count = [0]*26
        # a = ord("a")
        # for char in s:
        #     s_count[ord(char) - a] += 1  

        # alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        # s_builder = []
        # for char in list(order) + alpha:
        # # for char in list(order) + list(string.ascii_lowercase):
        #     i = ord(char) - a
        #     if s_count[i]:
        #         for _ in range(s_count[i]):
        #             s_builder.append(char)
        #         s_count[i] = 0
        
        # return "".join(s_builder)
