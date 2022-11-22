# Initial instinct: Counter for chars in string,
# compare sorted lists of strings counter values (ignore keys)


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # neat but slow
        return len(set(s)) == len(set(t)) == len(set(zip(s, t)))


# #doesnt need to convert or compare strings at the end
# #exits on first failure
# #still slower?
#         if len(s) != len(t):
#             return False

#         s_to_t = dict()
#         used_t = set()

#         # for s_char, t_char in zip(s, t):   #"clever" but slow?
#         for i in range(len(s)):
#             if s[i] not in s_to_t:
#                 if t[i] not in used_t:
#                     s_to_t[s[i]] = t[i]
#                     used_t.add(t[i])
#                 else:
#                     return False
#             elif s_to_t[s[i]] != t[i]:
#                 return False

#         return True


# this processes the whole string and does other unnecessary work
# along the way. We can build the dictionary ourselves and
# fail sooner if needed.

#         s = list(s)
#         t = list(t)
#         if len(s) != len(t):
#             return False

#         #create a relation from t to s
#         t_to_s = dict(zip(t,s))

#         #Fail if the relation is not Injective
#         #(different elements in T point to the same element in S)
#         if max(Counter(t_to_s.values()).values()) > 1:
#             return False

#         #convert t to s using the map
#         for idx, char in enumerate(t):
#             t[idx] = t_to_s[char]

#         return s == t
