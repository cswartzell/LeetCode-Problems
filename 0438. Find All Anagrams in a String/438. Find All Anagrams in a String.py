s = "abab"
p = "ab"

angrms_i = []
correct = list(p)
incorrect = []
left = 0
right = 0

while right < len(s):
    if s[right] in correct:
        correct.remove(s[right])
    else:
        incorrect.append(s[right])
    if right >= len(p):
        if s[left] in incorrect:
            incorrect.remove(s[left])
        else:
            correct.append(s[left])
        left += 1
    if correct == [] and incorrect == []:
        angrms_i.append(left)
    right += 1

print(angrms_i)


# aha! We dont care about the order of the letters, so we can simply slice, sort, and compare both substrings
# Damn! Still too slow. It is slicing and SORTING substring of len(p) n - p times: sort(sp-p)
# and I have no idea how bad the sorting step is. presumably nlogn

# angrms_i = []
# p_angrms = sorted(list(p))
# p_len = len(p)

# for i in range( len(s)-p_len + 1 ):
#     if sorted(s[i:i+p_len]) == p_angrms:
#         angrms_i.append(i)

# print( angrms_i )


# Nope: The following only works if there are no duplicate letters

# angrms_i = []
# p_angrms = set(p)

# for i in range(len(s)):
#     if set(s[i:i+len(p)]) == p_angrms:
#         angrms_i.append(i)

# print(angrms_i)
