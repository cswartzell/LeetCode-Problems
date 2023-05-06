"""07-13-2022 LeetCode 32. Longest Valid Parentheses"""

# as the only two allowable chars are '(' and ')' any valid substring
# regardless of length must have "()" somewhere in its midst. Removing that
# would not change the validity of an larger string containing this substring,
# and would have the effect of collapsing the next level (if any) of a container
# string to "()". We can do this iteratively to collapse all larger sets "((()))"
# For side by side valid substrings "()()" we replace each with a score, '1'.
# Side by side scores get added together. "()()()" -> "111" -> "3".
# collapsing pairs dont get deleted, but rather add a '1' to the space between them:
# ")(())()" -> ")(1)(" -> ")2(". By repeatedly applying these we should end up with a
# single highest score in the string

# Big O might be too high here, we are repeatedly scanning the list. There is probably
# an O(n) Solution. I strongly suspect TLE but want to start with these methods as
# maybe they will be useful in a single scan

# And I was right. This DOES work, but its O(n*2) I think. It restarts every time.
# I could have it process the list and restart if ANY changes were made, but thats
# probably still O(n**2). I had kind of a neat index manipulation thing going on,
# it may have actually worked where whenever a change is made you propogate backward
# *some* amount, but I got pretty lost as it ALWAYS might need to get back to the
# beginning, so it might not be able to just move back a fixed amount...
# What if every time a change is made it goes back to the first "("? Then I'm traversing
# forward and backward... and its STILL might be O(n**2)


# The following is straight from the answers
# class Solution:
#     def longestValidParentheses(self, s: str) -> int:
#         max_sub = 0
#         stack = [-1]
#         for i in range(len(s)):
#             if s[i] == "(":
#                 stack.append(i)
#             else:
#                 temp = stack.pop()
#                 if not stack:
#                     stack.append(i)
#                 else:
#                     max_sub = max(i - stack[-1], max_sub)

#         return max_sub


print('abc')

# class Solution:
#     def longestValidParentheses(self, s: str) -> int:
#         if len(s) < 2:
#             return 0
#         s = list(s) #convert to list as strings are immutable

#         #snip invalid ends ")))....(((". Only have to check these elements once, so
#         #probably cannot be further optimized
#         start = 0
#         end = len(s) - 1
#         while start <= end and s[start] == ')':
#             start += 1
#         while end >= 0 and s[end] == '(':
#             end -= 1
#         s = s[start:min(end + 1, len(s))]

#           #scan the list for ()
#         i = 0
#         go_back = False
#         while i < len(s)  - 1:
#             if s[i] == '(':
#                 curr = i + 1
#                 while curr < len(s)-1 and type(s[curr]) == int:
#                     curr += 1
#                 if s[curr] == ')':
#                     s = s[:i] + [2] + s[i+1:curr] + s[curr+1:]

#                     go_back = True      #This here sucks. It's at least O(n**2) as it starts over whenever there is a change.
#                                         #I could run through the entire list and THEN start over if there were any changes
#                                         #but that might be just the same if the change was always the last pair
#                     # i = max(i-1,0)
#             while i < len(s) -1 and type(s[i]) == type(s[i+1]) == int:
#                 s[i] += s[i+1]
#                 s = s[:i+1] + s[i+2:]
#             i = 0 if go_back else i + 1
#             go_back = False

#         sub_max = 0
#         for x in s:
#             if type(x) == int:
#                 sub_max = max(sub_max,x)
#         return sub_max
