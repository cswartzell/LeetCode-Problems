# 12-05-2022 Leetcode 38. Count and Say
# https://leetcode.com/problems/count-and-say/

# Oh neat, I just learned about this sequence from Matt Parkers
# youtube channel. I liked the name he gave for it better,
# "See and Say"

# Ok, lets use a stack to store each digit and number of repititions
# Then, just build up the string using a list comprehension


class Solution:
    def countAndSay(self, n: int) -> str:
        curr_string = "1"
        for N in range(n - 1):
            s_stack = []
            i = 0

            while i < len(curr_string):
                curr_digit = curr_string[i]
                curr_repeats = 1
                i += 1
                while i < len(curr_string) and curr_string[i] == curr_digit:
                    curr_repeats += 1
                    i += 1
                s_stack.append((curr_digit, curr_repeats))

            curr_string = "".join([str(repeat) + digit for digit, repeat in s_stack])

        return curr_string
