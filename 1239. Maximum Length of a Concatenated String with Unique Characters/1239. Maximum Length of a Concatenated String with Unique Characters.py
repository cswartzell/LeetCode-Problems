# 03-28-2023 leetcode 1239. Maximum Length of a Concatenated String with Unique Character
# https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/description/

#First: two basic approaches: 
# 1: just use sets and set intersection. Resonably fast, its just chars after all
# 2: convert the substrings to binary and use binar operations such that A or B == 0
# MUCH faster operation, but more overhead to create.  
# Binary strings are a reasonable len at only 26 bits. There are 16 possible substrings,
# and so combinations of any len of any of them is nontrivial: 16choose0 + 15choose1 + 14choose2...
# Ok, binary comparisons it is. 

# Then... how to check them. Do I need to check ALL of the potential combinations? That seems 
# unlikely, but possible. In the SET version we might be able to start with len. Can we be
# greedy? Greedy-ish? Not as easy witthe binary version. Wed have to count ones in the number
# which kinda defeats the purpose. Maybe we could sort them before converting to binary
# and just retain that order on processing? Better get started...

# Cant be naively greedy. Combining ABC with DEF would prematurely preclude say FGHIJ
# Which is clearly longer. Ugh, recursively OR them in?

# Can I sort them by len first, then check iteratively from the start oring as we go?
# restarting each time? so 4&3&2&1 and 3&2&1 and 2&1... ? Im not positive, but could start
# that way

#Otherwise its 2^16 combinations which seems like a bit much to check, but I suppose is possible
# Wait, thats only 65,500ish to start with. Really not bad at all. Maybe faster to just check and
# NOT sort? Unfortunately getting the hamming weight is not instant really. 

# import itertools
# import functools

class Solution:
    def maxLength(self, arr: List[str]) -> int:        
        # Use depth first search recursion through arr
        # building from an initial empty string
        return self.dfs(arr, 0, "")
    
    def dfs(self, arr: List[str], pos: int, res: str) -> int:        
        # Use a set to check res for duplicate characters
        if len(res) != len(set(res)):
            return 0

        # Recurse through each possible next option
        # and find the best answer
        best = len(res)
        for i in range(pos, len(arr)):
            best = max(best, self.dfs(arr, i + 1, res + arr[i]))
        return best




# class Solution:
#     def maxLength(self, arr: List[str]) -> int:
#         arr_bin = []        
#         # arr.sort(key= lambda x : len(x), reverse= True)
#         max_len = 0

#         for sub_str in arr:
#             sub_str_set = set(sub_str) 
#             #It doesnt specify arr[i] is comprised of unqique characters explicitly
#             #AHA! In fact the examples INCLUDE strings that are composed of non unique letters.
#             #We can IGNORE this entirely, their inclusion would automatically break uniqueness
#             if len(sub_str) != len(sub_str_set):
#                 continue
#             #Get the max length of a single sub_str now, otherwise we may need to check 2^17 instead of 2^16 later
#             max_len = max(max_len, len(sub_str_set))
#             bin_str = 0
#             for letter in sub_str:
#                 bin_str |= (1 << ord(letter))
#             arr_bin.append(bin_str)
        
#         valid = set(arr_bin)
#         q = collections.deque(arr_bin)
#         while q:
#             combo = q.popleft()
#             for bin_str in arr_bin:
#                 if not bin_str & combo:
#                     orred = bin_str | combo
#                     if orred not in valid:
#                         valid.add(orred)
#                         q.append(orred)
#                         max_len = max(max_len, bin(orred).count("1"))

        #BOLLOCKS! Getting the hamming weight is correct here, but I guess you cant be greedy.
        # for i in range(len(arr_bin)):
        #     curr_bin = arr_bin[i]
        #     for j in range(i + 1, len(arr_bin)):
        #         if curr_bin & arr_bin[j] != 0:
        #             continue
        #         else:
        #             curr_bin |= arr_bin[j]
        #     max_len = max(max_len, bin(curr_bin).count("1"))



        # def or_if_not_and(x, y) -> int:
        #     return x |= y if x & y == 0 else 0

        # def hamming_w(x) -> int:
        #     return bin(x).count("1")


        return max_len
