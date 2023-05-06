# Start by identifying which string is longer. This maybe? is useful
# Great, ignore that for now maybe?
# Make all 3 (or maybe just s1, s2) into deques for speeds
# Look at the next (first) letter in s3:
# if not in s1 or s2, return False
# if only in s1, consume it and continue
# if only in s2, consume it and continue
# else while in BOTH
#    consume from both but add to a stack
#    repeat until one of three cases:
#       we run out of letters in both stacks (I think impossible since len.s1 != len.s2)
#       the next letter in s3 is not in either s1 or s2 next (return False)
#       the next letter in s3 is in only s1 or s2. Consume it from the correct string
#       prepend our letter stack to the string that DIDNT have the next s3 letter
#       exit the while
# return True (implicitly true as we never hit a failure)

# Oh, if I do the while loop first, it will handle the 3 cases once falling out of the loop

from collections import deque


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        if not s3:
            return True
        dp = [False for _ in range(len(s2) + 1)]

        for i in range(len(s1) + 1):
            for j in range(len(s2) + 1):
                if i == 0 and j == 0:
                    dp[j] = True
                elif i == 0:
                    dp[j] = dp[j - 1] and s2[j - 1] == s3[i + j - 1]

                elif j == 0:
                    dp[j] = dp[j] and s1[i - 1] == s3[i + j - 1]

                else:
                    dp[j] = (dp[j] and s1[i - 1] == s3[i + j - 1]) or (
                        dp[j - 1] and s2[j - 1] == s3[i + j - 1]
                    )

        return dp[len(s2)]


# The following is so goddamned close I can feel it, but it fails consistently. I strongly suspect its just
# a minor flaw in logic rather than a complete mistake... I think I cant consume from the "in_both" queue ever

#         #using a deque instead of reversing it and using a stack as I like to see it in the original context
#         s1, s2, s3 = deque(s1), deque(s2), deque(s3) #could be done with 2 pointers each instead of stacks
#         in_both = deque()

#      #   for next_letter in range(len(s3)):    #BAH! Thats right, you cannot modify the loop var IN the loop
#         next_letter = s3.popleft()
#         while True:          #catch when one deque is empty
#             if  (not s1 or s1[0] != next_letter) and (not s2 or s2[0] != next_letter):  #WAS AN IF AT HEAD before above if, now elif
#                     return False
#             elif s1 and s2 and s1[0] == s2[0] == next_letter:
#                 in_both.append(next_letter)
#                 s1.popleft()
#                 s2.popleft()
#                 # next_letter = s3.popleft() #I dont think I need to test if there is s3 left, there must be
#                                         #as to get to here there had to be at least 1 letter in s1 and s2 and s3 == len.s1 + len.s2
#             # elif in_both and next_letter == in_both[0] and (next_letter == s1[0] or next_letter == s2[0]):
#             #     in_both.popleft()
#             elif s1 and s1[0] == next_letter and (not s2 or s2[0] != next_letter):
#                 s1.popleft()
#                 if in_both:
#                     s2.extendleft(in_both)
#                     in_both.clear()
#             elif s2 and s2[0] == next_letter and (not s1 or s1[0] != next_letter):
#                 s2.popleft()
#                 if in_both:
#                     s1.extendleft(in_both)
#                     in_both.clear()
#             if s3:
#                 next_letter = s3.popleft()
#             else:
#                 break

#         return True
#     #(s1.extendleft(in_both) == s3 or s2.extendleft(in_both) == s3)
