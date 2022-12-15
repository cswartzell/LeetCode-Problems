# 12-14-2022 1143. Longest Common Subsequence
# https://leetcode.com/problems/longest-common-subsequence/description/

# Lets see... firstly, we literally dont care about chars that arent part of
# both. We want to retain their orders though. We can make a set of chars that
# are in both and eliminate all other chars in each string, thus shortening
# each string. Unfortunately string concatentation sucks so we'll need to
# use a string builder. We do need to keep all copies of pertininet letters
# in their original order. Oh wait. We DONT need to keep duplicates of the
# SAME letter in the order, they can be compressed to be a single copy....
# no, thats not true. One string CAN have duplicates "aaab" in "aaaaaabbb"


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        common_letters = set(text1).intersection(set(text2))
        # catches 0 or 1 common substrings
        # if len(common_letters) < 2:
        #     return len(common_letters)

        # new_t1 = [x for x in text1 if x in common_letters]
        # new_t2 = [x for x in text2 if x in common_letters]

        # if len(new_t1) < len(new_t2):
        #     shorter, longer = new_t1, new_t2
        # else:
        #     shorter, longer = new_t2,new_t1

        # longer_indexes = collections.defaultdict(collections.deque)
        # for val, key in enumerate(longer):
        #     longer_indexes[key].append(val)

        # max_len = 0
        # curr_len = 0
        # last_i = 0

        # for x in shorter:
        #     if longer_indexes[x][-1] >= last_i:
        #         curr_len += 1
        #         while longer_indexes[x] and longer_indexes[x][0] <= last_i:
        #             last_i = longer_indexes[x][0]
        #             longer_indexes[x].popleft()
        #     else:
        #         curr_len = 1
        #         last_i = longer_indexes[x][0]
        #     max_len = max(max_len, curr_len)

        # return max_len


# class Solution:
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:

#         # If text1 doesn't reference the shortest string, swap them.
#         if len(text2) < len(text1):
#             text1, text2 = text2, text1


#         # The previous column starts with all 0's and like before is 1
#         # more than the length of the first word.
#         previous = [0] * (len(text1) + 1)

#         # Iterate up each column, starting from the last one.
#         for col in reversed(range(len(text2))):
#             # Create a new array to represent the current column.
#             current = [0] * (len(text1) + 1)
#             for row in reversed(range(len(text1))):
#                 if text2[col] == text1[row]:
#                     current[row] = 1 + previous[row + 1]
#                 else:
#                     current[row] = max(previous[row], current[row + 1])
#             # The current column becomes the previous one.
#             previous = current

#         # The original problem's answer is in previous[0]. Return it.
#         return previous[0]
