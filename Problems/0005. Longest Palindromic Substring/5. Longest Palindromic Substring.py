# -----------------------------------------------------------------------------------------------------------
# had to look at solutions to learn how to do better.
# couldnt think programatically of a clear better algortim, but I did have the jist
# of the following componnents at one time. I need to know more about DP to
# understand how to derive these from the get got

# ok, we are going to check OUT from the center of each char in the string
# Its kind of like an exploding sliding window. Start w/win_len = 1
# expand while its a palindrome, record the longest result, slide window
# and reset its length to 1. Notably we have to "half slide" the window
# to check palindromes centered on a char, or between two chars
s = "cbbd"

longest_pal = s[0]

for i in range(len(s) - 1):
    l, r = i, i + 1  # reset pointers to the left and right of the window
    # adding one to check EVEN length pals, centered BETWEEN two letters
    while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
        if r - l + 1 > len(longest_pal):
            longest_pal = s[l : r + 1]
        l -= 1
        r += 1

    l, r = i - 1, i + 1  # pointer to the left and right of the window
    # checks palindromes of ODD length, centered on and ignoring i
    # (we dont need to check again for trivial length 1)
    while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
        if r - l + 1 > len(longest_pal):
            longest_pal = s[l : r + 1]
        l -= 1
        r += 1

# print(longest_pal)


# -----------------------------------------------------------------------------------------------------------


# 2-6-21: Ok, going to start with with a naive approach... just to do it
# start with the full array and compare with the reverse. Then look at
# each array of n-1 length etc. Return number of iterations on first palindrome

#!And indeed it works, and times out on large data sets.
# slicing a substring backwards to INCLUDE the first letter is tough
# this is some seriously covoluted indexing
# s = "123456"
# k = s[len(s) - 1]
# l = s[-1 : -len(s) - 1 : -1]
# x = s[len(s) :: -1]
# i = 5
# j = 0
# # so want the reverse of 345 -> 543, to start 5 is len(s) - i + j, and the stopping point is len(s) - i
# yf = s[j : i + j]
# yrev = s[len(s) : -0 : -1]
# d = "fiddlesticks"
# for i in range(len(s), 1, -1):
#     for j in range(0, len(s) - i + 1):
#         forward = s[j : i + j]
#         backward = s[
#             -len(s) + i - 1 + j : -len(s) + j - 1 : -1
#         ]  # BOY IS THAT A MOUTHFULL!
#         # A slice, starting from its negative length -1
#         if forward == backward:
#             print(i)


# for i in range(len(s), 1, -1):
#     for j in range(0, len(s) - i + 1):
#         forward = s[j : i + j]
#         backward = s[-i:-j:-1]  # BOY IS THAT A MOUTHFULL!
#         # A slice, starting from its negative length -1
#         if forward == backward:
#             print(i)
