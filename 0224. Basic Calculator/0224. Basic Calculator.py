# 11-19-2022 LeetCode 224. Basic Calculator
# https://leetcode.com/problems/basic-calculator/

# Start by identifying possible scenarios:
# num + num
# num - num
# (EXPRESSION) evaluate inside, becomes num
# -(Expression) multiply num by -1, Can only be at front
# of a block: either the first space, or first space inside
# of parens. WITHIN a block this can only mean subtraction
# num - (expression), no different from just subrtacting
# -num: multiply num by -1, Can only be at the front
# of a block: either the first space, or first space inside
# of parens. WITHIN a block this can only mean subtraction

# The spaces dont help, so lets strip them.

# Weird idea #1: enclose the intial expression in parens
# Scan forward until we reach a close paren, delete it,
# sum and subtract our way backwards til the first open paren.
# Delete that and begin scanning forward. This should always
# evaluate the innermost parens ahead of outer ones, and LASTLY
# evaluate the initial expression.

# Is that just the equivalent of the following?
# create a stack that is num, operation, num, operation...
# (or, like reverse Polish, num num num.... operation operation op...)
# 1: Determine if it leads with a -
# If so, push -1 for the first num
# push the value if followed by a num

# 3-(2-1) != 3-2-1

# It says s consists "of digits" but is not clear if this is single digits
# or if multiple digits are allowed. Assume the latter I guess?
# Example cases use up to 10, but weirdly no higher


# Well damn. My solution works, but TLE for very large input.
# How can we improve? Well there is not really a need to
# compute ADDING a paren expression, thats just the same
# as ignoring the parens. We only care about subtracting
# paren expressions. Also, subtracting a parens expresstion
# IS the same as adding the opposite sign of everything inside
# Could we perhaps swap the signs on every element within -(),
# then just evaluate as is (ignore +())? We have to account for
# nested parens again...


# 3-(2+1-(4+(-5))) #ADD + after all open Parens


class Solution:
    def calculate(self, s: str) -> int:
    # no need to ACTUALLY add them, we pass the paren-stripped middle
    # to the "eval parens" function, so can just pass the initial s
    # s = "(" + s + ")"

    #remove spaces
    s = s.replace(" ", "")

    def eval_parens( s ) -> int:
        #build stack of nums and operations for current string
        #Math stack should ALWAYS take the form Num(, Op, Num)...
        math_stack = collections.deque()
        i = 0
        #I THINK this can only happen here, at the start of a 'block'
        #noting if we recurse to go within a new paren set, thats the
        #head of a new 'block' as well
        if s[i] == "-":
                math_stack.append(-1)
                math_stack.append("*")
                i += 1
        while i < len(s):
            if s[i] in string.digits:
                curr_num = ord(s[i]) - 48
                while i < len(s) - 1 and s[i+1] in string.digits:
                    i += 1
                    curr_num *= 10
                    curr_num += ord(s[i]) - 48
                math_stack.append(curr_num)
            elif s[i] == "+":
                math_stack.append("+")
            elif s[i] == "-":
                math_stack.append("-")
            elif s[i] == "(":
                open_parens = 1
                j = i + 1
                while open_parens != 0:
                    if s[j] == "(":
                        open_parens += 1
                    if s[j] == ")":
                        open_parens -= 1
                    j += 1
                math_stack.append(eval_parens(s[i+1:j-1]))
                i = j-1
            i += 1
        #compute math_stack
        num_A = math_stack.popleft()
        while math_stack:
            op, num_b = math_stack.popleft(), math_stack.popleft()
            if op == "*":
                num_A *= num_b
            elif op == "+":
                num_A += num_b
            elif op == "-":
                num_A -= num_b
        return num_A
    return eval_parens(s)
