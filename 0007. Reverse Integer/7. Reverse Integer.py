"""02-10-2022 LeetCode 7. Reverse Integer"""
# x = 2147483647    #MAX_INT
# x = -2147483648    #MIN_INT
# x = 7463847412    #MAX_REV_INT
# x = 8463847412    #REV_OVERFLOW
x = -9463847412  # REV_UNDERFLOW
# x = -8463847412  # MIN_REV_INT
# x = 1534236469
# class Solution:
#     def reverse(self, x: int) -> int:
save_sign = 1  # work with only positive ints, save the sign bit
if x < 0:  # which gives us room for aan overflowbit buffer which we'll check
    save_sign *= -1
    x = x * -1

temp = 0
rev_x = 0
digi_count = 0
while x:
    temp = x % 10
    x = x // 10  # ooh, saw this bad boy on a page and want to give it a whirl
    # integer division, truncates and returns int instead of float
    if digi_count < 9:  # we know that a 10 digit int is over MAX_INT
        rev_x = (rev_x * 10) + temp
    elif (save_sign == -1) and (rev_x > 214748364 or (rev_x == 214748364 and temp > 8)):
        rev_x = 0  # if we are negative, and rev is > MIN_INT less last digit, or
        # MIN_INT less last digit is spot on, but the last digit is too high
        # return 0
    elif (save_sign == 1) and (rev_x > 214748364 or (rev_x == 214748364 and temp > 7)):
        rev_x = 0  # same logic as above (are we at, or above MAX_INT)?
    else:
        rev_x = (rev_x * 10) + temp
        # ok, we add the last 9 digit number as we are between MIN and MAX int

    digi_count += 1

# return (rev_x * save_sign) #restore the sign bit


print(rev_x * save_sign)
