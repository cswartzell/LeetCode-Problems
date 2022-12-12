# 12-11-2022 Leetcode 22. Generate Parentheses
# https://leetcode.com/problems/generate-parentheses/description/

# If at open_parens_sum zero, with n-i parens left to place, we can ONLY
# place an open paren. Similarly, when twe open_parens_sum is n-i with
# only i more spaces to place, we may ONLY close parens then on.
# anytime inbetween we may do either (or rather DO Both).
# Sounds like a stack problem

# I bet there is a far more clever binary way to do this, but I'm proud
# of this iterative stack solution that more or less worked exactly
# as I described


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        parens_stack = [["(", 1]]
        i = 0

        for i in range(2 * n - 1):
            next_stack = []
            while parens_stack:
                parens, open_pairs = parens_stack.pop()
                if open_pairs == 0:
                    next_stack.append([parens + "(", open_pairs + 1])
                elif 2 * n - i - 1 == open_pairs:
                    parens += ")"
                    next_stack.append((parens, open_pairs - 1))
                else:
                    next_stack.append([parens + "(", open_pairs + 1])
                    next_stack.append([parens + ")", open_pairs - 1])
            parens_stack = copy.copy(next_stack)

        return [x[0] for x in parens_stack]
