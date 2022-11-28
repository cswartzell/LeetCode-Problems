# 11-27-2022 Leetcode 150. Evaluate Reverse Polish Notation\
# https://leetcode.com/problems/evaluate-reverse-polish-notation/description/

# pretty straight forward stack problem
# A tiny part of me wants to beceome an RPN evangelist, but
# I know my hearts not in it and I wont become "fluent" in it
# to do it as quickly. I love me too many parens anyhow.


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        rp = []
        for token in tokens:
            if token not in {"+", "-", "*", "/"}:
                rp.append(int(token))
            else:
                # ooh, good question. What gets evaluated first?
                num_b, num_a = rp.pop(), rp.pop()
                # ooh switches are finally a thing.
                match token:
                    case "+":
                        rp.append(num_a + num_b)
                    case "-":
                        rp.append(num_a - num_b)
                    case "*":
                        rp.append(num_a * num_b)
                    case "/":
                        rp.append(int(num_a / num_b))
                    # Note: the // operator is same as floor(x/y) WHICH GETS THE NEXT
                    # LOWER NUMBER, meaning DOWN for negative. Not truncation
        return rp[0]
