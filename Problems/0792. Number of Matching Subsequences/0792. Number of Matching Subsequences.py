# My initial instinct is to start a dictionary with the letters as keys,
# and their index of position as an array for each letter.
# To search a word, start witht the lowest index for the first letter of the
# word, then the lowest index of the second letter that is higher than that of
# the first letter... and so on. Break out if we ever cant find a letter, no
# need to search the rest.
from collections import defaultdict


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:

        # someones solution. Lol, wut? Literally what is happening
        # Ok, so map takes a callable, in this case a defined method
        # It then passes the elements of an iterable to the method
        # explaining the lack of parens or passing the sub method input
        # Apparently this is basically cheater looping. BUT FASTER
        # It returns a map object, which must be unpacked
        # Here, sum is used to iterate the map object, which is just
        # bool values, so summing them gives you the number of matched words
        # THIS IS FUCKING BRILLIANT CODING

        # def sub(st):
        #     pos = -1
        #     for char in st:
        #         pos = s.find(char, pos+1)
        #         if pos == -1: return False
        #     return True
        # return sum(map(sub, words))

        # from solutions:
        # # String find is SIGNIFICANTLY faster than looping through each character yourself.

        # s_dict = defaultdict(lambda:[5001])
        # for i in range(len(s)):
        #     if s[i] not in s_dict:
        #         s_dict[s[i]] = [i]
        #     else:
        #         s_dict[s[i]].append(i)
        # s_dict.setdefault(lambda:[5001])
        num_words_found = 0

        for word in words:
            num_words_found += 1
            pos = -1
            for i in range(len(word)):
                pos = s.find(word[i], pos + 1)
                if pos == -1:
                    num_words_found -= 1
                    break

        return num_words_found


# Im a little crushed that my dict method here failed. Ill try to tweak it.

#         s_dict = defaultdict(lambda:[5001])
#         for i in range(len(s)):
#             if s[i] not in s_dict:
#                 s_dict[s[i]] = [i]
#             else:
#                 s_dict[s[i]].append(i)
#         s_dict.setdefault(lambda:[5001])


#         for word in words:
#             last_seen_idx = -1
#             num_words_found += 1
#             for letter in word:
#                 temp = [i for i in s_dict[letter] if i > last_seen_idx] + [5001]
#                 last_seen_idx = temp[0]
#                 if last_seen_idx == 5001:
#                     num_words_found -= 1
#                     break

#         return num_words_found
