s1 = "ab"
s2 = "eidbaoxkt"

win_left = 0
win_right = len(s1)

s1_permutations = set(s1)

while win_right <= len(s2):
    s2_sub = set(s2[win_left:win_right])
    if s1_permutations == set(s2[win_left:win_right]):
        print("True")
        # return true
    win_left += 1
    win_right += 1
print("False")
# return false
