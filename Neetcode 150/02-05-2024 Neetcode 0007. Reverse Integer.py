# 02-05-2024 Neetcode 0007. Reverse Integer
# https://leetcode.com/problems/reverse-integer/
# Time:14 Challenge: 4/5

# imma just do it with strings. Easier right?
# I see I made an error last time, you CANNOT calculate 2**31 - 1
# or... you can but its wacky. In a system with fixed integers it will 
# first do the full multiplication 2*31. This will result in an overflow.
# and be equivalent to 1 with 31 zeros after it = -(2**31) which we CAN
# store. We then subtract 1 and UNDERFLOW and end up with the right answer
# This is kind of neat, but may result in errors being thrown.
# Instead lets make sure there is NEVER over/underflow


class Solution:
    def reverse(self, x: int) -> int:
        max_int = 2*30 + (2*30 - 1)  #1 under 2*31
        max_prefix = max_int // 10
        min_int = -max_int - 1
        min_prefix = min_int // 10

        str_x = str(x)
        neg_sign = str_x[0] == "-"
        if neg_sign: 
            str_x = str_x[1:]

        # not enough digits to matter
        if len(str_x) < len(str(min_int)):
            rev_x = reversed(str_x)
            if neg_sign:
                rev_x = "-" + rev_x
            return int(rev_x)

        if str_x(len)





# Interesting. How to detect if something WILL overflow?
# One method is, do it. An exception may be thrown and thats our "clue"
# in which case we are just doing error handling. Another method, assuming
# it overflows silently, is to 'undo' the multiplication by performing the 
# reciprocal division on the result and see if you get the original number back
# or if overflow has caused mischief. Lastly, we can manually check if the result
# will exceed our bounds by noting a little math fact:
# if a * b > max_int, then clearly a > max_int/b. We can of course do the reverse, 
# but as multiplication is associative, we actually dont need too.
# We can do the same for the negative end. Thus, we will know PRIOR to performing the
# overflow error that it will result and can immediately return 0

# Hmm... this all seems fine excpet the bit about negative numbners... How does mod work
# with them? OH WOW. After doing a brief test the answer is WAY DIFFERENT THAN YOU THINK.
# -12 % 10 8, and -123 // 10 = -13, not -12. It does the negative for you  and rounds down.
# this is not AT ALL useful. We need to convert to positive. HOWEVER, note MIN_INT
# CANNOT be converted to MAX_int, it is 1 too large and will thus immediately overflow.
# We will have to handle it seperately. Luckily, its reverse would overflow so we can just
# return 0 instead. Then simply negate it, and treat is like the positive case WITH THE
# DIFFERING MIN_INT/MAX_MULT_NEG


class Solution:
    def reverse(self, x: int) -> int:
        MAX_INT = 2**31 - 1             #  2147483647
        MIN_INT = 2**31                 # -2147483648 INTENTIONALLY non-negative
        MAX_MULT = MAX_INT // 10    #  0214748364
        answer = 0

        if x == MIN_INT:
            return 0 
        if x <= 9 and x >= -9:
            return x 

        is_neg = 1
        if x < 0:
            is_neg = -1
            x = -x
        while x:
            digit = x % 10
            x //= 10
            if answer <= MAX_MULT:
                answer *= 10
            else: 
                return 0
            if answer <= MAX_INT - digit:
                answer += digit
            else:
                return 0

        return answer * (is_neg)
