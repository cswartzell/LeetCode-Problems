import math

x = 10001

msdpower = 0
while x // 10 ** msdpower >= 10:
    msdpower += 1

middle = msdpower / 2

for i in range(msdpower - math.floor(middle) + ((msdpower + 1) % 2)):
    left_digit = (x // 10 ** (math.ceil(middle + i))) % 10
    right_digit = (x // 10 ** (math.floor(middle - i))) % 10
    if left_digit != right_digit:
        returnfalse = False
        break

print("returntrue")


# first method is to convert to string
# x = 121
# print(str(x) == str(x)[::-1])

# ah, but the problem asks if I can do it without converting to a string
# I suppose I could convert it to a list by mod/div 10 but really how is
# that different than manually converting to a string? Oh, because I dont
# have to store the whole thing, and can just compare the first and last
# digits and discard, so constant space
# How to get the most significant digit though? I can iterate and divide
# by powers of 10 until I get 1 < x < 10 (truncate the result). It works
# but I wouldnt exactly call it clever.

# well fuck. Of course this method ignores leading zeros... which we cannot
# ignore once we start removing the msd. Ok fine... we can salvage it
# we WONT remove the msd, but instead figure out the highest order for the
# msdpower, then iterate i through each msd round less than this
# OR we could check if the next msd is a zero and perform a miniloop checking
# for lead/trailing zero matches, breaking if not matched in CONJUNCTION with
# removing the lsd/msd?

# x = 1000001
# ans = True

# while x >= 10 and ans == True:
#     lsd = x % 10
#     msdpower = 1
#     while x // 10 ** msdpower >= 10:
#         msdpower += 1
#     msd = x // 10 ** msdpower
#     if msd != lsd:
#         ans = False
#         break
#     else:
#         didthiswork = (x // 10 ** (msdpower - 1)) % msd * 10
#         while (x // 10 ** (msdpower - 1)) % msd * 10 == 0: #THIS IS CLOSE BUT OFF> FIX IT
#             # catches 2nd msd == 0
#             x = x // 10
#             lsd = x % 10
#             if lsd != 0:
#                 ans = False
#                 break
#             msdpower -= 1
#         x = (x - (msd * 10 ** msdpower)) // 10

# print(ans)
