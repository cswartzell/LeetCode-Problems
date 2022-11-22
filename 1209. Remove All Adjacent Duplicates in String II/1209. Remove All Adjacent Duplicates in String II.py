# String slicing to the rescue. Seems pretty simple
# using a two pointer solution.
# Oh wait, collapsing strings can cause a sort of
# chain combo effect that precededs the left most
# pointer. I think we may need to go back k or
# possibly k-1 spaces after each delete to recheck
# previous areas. That or check backwars for matches
# each time, but that seems tedious to deal with direction
# and is probably only marginally more efficient?
# I guess for high k its actually significantly better
# as a single test can break the check, where jumping back
# requires each and every char to be checked again...


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for each in s:
            if len(stack) == 0:
                stack.append([each, 1])
            elif each == stack[-1][0]:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    del stack[-1]  # pop the k dups
            else:
                stack.append([each, 1])
        return "".join([x[0] * x[1] for x in stack])


# Ok, im going to give up on the following overly clever solution:
# I think it might be done, but now it times out so posisbly an infinite loop
# I liked the idea of a drunkards walk, rather than just jumping back
# k spaces once you delete a match. For LONG matches that would be super wasteful,
# we know there is no reason to check the previous K letters unless the two halves
# coming together are the same char, otherwise the previous k matches would have already
# been deleted... so why not count and match backwards after each delete, and jump to the
# right pointer if we fail a match? MUCH more efficient for large sparse K... which is not
# at all what the test cases have. This is a LOT of work for small k...


# class Solution:
#     def removeDuplicates(self, s: str, k: int) -> str:
#         l_ptr = 0
#         r_ptr = min(l_ptr + 1, len(s) -1)

#         rev_dir = 1
#         t  = ""

#         while l_ptr != r_ptr:

#             zzL = s[l_ptr]
#             zzR = s[r_ptr]

#             if s[l_ptr] == s[r_ptr]:
#                 if r_ptr - l_ptr + 1 == k:
#                     t = s[:l_ptr]
#                     if r_ptr + 1 < len(s):       #stupid req of string slicing...
#                         t += s[r_ptr + 1:]
#                     s = t[:]                    #does this assign by val instead of ref? YES
#                     l_ptr = max(l_ptr - 1, 0)   # Prevent l_ptr going before beginning of s
#                     r_ptr = min(l_ptr + 1, len(s) -1) # Prevent r_ptr going after end of s
#                     rev_dir = -1
#                 elif  rev_dir == 1:
#                     while r_ptr < len(s) - 1 and s[l_ptr] == s[r_ptr + 1]and r_ptr - l_ptr + 1 < k:
#                         r_ptr += 1
#                     if r_ptr - l_ptr < k - 1:
#                         l_ptr, r_ptr = min(r_ptr-1, len(s)-1), min(r_ptr, len(s)-1)
#                 elif  rev_dir == -1:
#                     while l_ptr > 0 and s[l_ptr-1] == s[r_ptr] and r_ptr - l_ptr + 1 < k:
#                         l_ptr -= 1
#                     rev_dir = 1
#             else:
#                 rev_dir = 1
#                 l_ptr += 1
#                 r_ptr = min(l_ptr + 1, len(s) -1)
#         return s
