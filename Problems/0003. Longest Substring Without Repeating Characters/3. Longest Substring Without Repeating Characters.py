# No need for guard clause, now handles sets of length 0
# if len(s) == 0:
#     return 0
s = "aosjdhaqwertyuiopoksiudhfoia1234567"

tmp_set = set()
win_left = 0
win_right = 0
max_win = 0

while win_right <= len(s) - 1:
    if not s[win_right] in tmp_set:
        tmp_set.add(s[win_right])
        win_right += 1
        if max_win < win_right - win_left:
            max_win += 1
    else:

        tmp_set.remove(s[win_left])
        win_left += 1
print(f"The longest substring of unique chars in '{s}' is '{max_win}' chars")
# #-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# s = "abcdabecbd12345"

# tmp_dict = {s[0]:s[0]}
# win_left = 0
# win_right = 0
# max_win = 1

# while win_right <= len(s) - 2:
#     if not s[win_right + 1] in tmp_dict:
#         win_right += 1
#         if max_win < win_right - win_left + 1:
#             max_win += 1
#         tmp_dict.update({s[win_right]:s[win_right]})
#     else:
#         win_left += 1
#         tmp_dict.clear()
#         for chars in range(win_left, win_right + 1):
#             tmp_dict.update({s[chars]:s[chars]})
# #-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# s = "abcdabecbd12345"

# win_left = 0
# win_right = 0
# max_win = 1

# sub_unique = True
# tmp_list = []
# i = 0

# while True:
#     while i <= win_right:
#         if s[i] in tmp_list:
#             sub_unique = False
#         else:
#             tmp_list.append(s[i])
#         if sub_unique and i == win_right and win_right < len(s):
#             win_right += 1
#             max_win = win_right - win_left
#         elif i == win_right and win_right < len(s) and win_left < win_right:
#             tmp_str = s[win_left + 1 : win_right + 1]
#             tmp_list.remove(s[win_left])
#             win_right += 1
#             win_left += 1
#             tmp_list.append(s[i])

#             j = 0
#             while j < max_win:
#                 if tmp_list.count(tmp_list[j]) > 1 and i < len(s):
#                     tmp_list.remove(s[win_left])
#                     win_right += 1
#                     win_left += 1
#                     j = 0
#                     i += 1
#                     tmp_list.append(s[i])
#                 j += 1
#             sub_unique = True
#         i += 1
#         if i > len(s) - 1:
#             break
#     break

# print(    f"The longest subsrting in '{s} is {max_win} chars, from index {win_left} to {win_right} '{s[win_left:win_right]}'")

3  # -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# THIS IS ... CLOSE, but not spot on. I suspect the POP off the dict is incorrect. Really, you need to pop one instance, but dict pop does not do that. I could use the val part of dict instead...
# if i cannot figure it out, I could always scrap tmp_dict and set i to move with the left window, rebuilding tmp_dict on each slide. It wouldnt even lose that much performance but still...
# what if i switch to a list? Supposedly i lose access to O(1) look ups, but lets try it to start

# s = "abcdabecbd123456"
# k = "0123456789012345"
#          l     r

# win_left = 0
# win_right = 0
# max_win = 1

# sub_unique = True
# tmp_dict = {}
# i = 0

# while True:
#     while i <= win_right:
#         if s[i] in tmp_dict:
#             sub_unique = False
#         else:
#             tmp_dict.update({s[i]: s[i]})
#         if sub_unique and i == win_right and win_right < len(s):
#             win_right += 1
#             max_win = win_right - win_left
#         elif i == win_right and win_right < len(s) and win_left < win_right:
#             tmp_str = s[win_left + 1 : win_right + 1]
#             if s[win_left] in tmp_dict:
#                 tmp_dict.pop(s[win_left])
#             win_right += 1
#             win_left += 1
#             i -= 1
#             sub_unique = True
#         i += 1
#         if i > len(s) - 1:
#             break
#     break

# print(f"The longest subsrting in '{s} is {max_win} chars")

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------THE FOLLOWING BRUTE FORCE METHOD WORKS, BUT IS VERY TIME/MEMORY COMPLEX----------
# Try smarter

# s = "abcabcbb"
# str_len = len(s)
# sub_unique = False
# longest_unique_sub = str(s[0])  # safe to initialize with single first char.

# for i in range(str_len, 0, -1):  # lenght of substring, starting with len(s) descending
#     for j in range((str_len - i + 1)):  # starting index of substring
#         tmp_str = s[j]  # first char of new tmp_str
#         for k in range(j + 1, i + j):  # iter for remainder of new tmp_str
#             tmp_str += s[k]
#         tmp_dict = {}
#         sub_unique = True
#         for char in tmp_str:
#             if char in tmp_dict:
#                 sub_unique = False
#                 break
#             else:
#                 tmp_dict.update({char: char})
#         if sub_unique:
#             longest_unique_sub = tmp_str
#             break
#     if sub_unique:
#         break
# print(f"The longest subsrting in '{s} is '{longest_unique_sub}' which is {len(longest_unique_sub)} chars")

# subsrtings = 0
# chars_total = 0  # guessing int overflow?
# for i in range(1, 5001):
#     subsrtings += i
#     chars_total += i * (5001 - i)
# print(f"{subsrtings} substrings in:")
# print(f"{chars_total/1000000000} GB, assuming only 1 byte per char. Could be 2 or even 4")
