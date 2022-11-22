""" 05-02-2022  Leetcode 844. Backspace String Compare"""

s = "#"
t = "#a#c"

# The first thing that comes to mind is that in Python strings are immutable
# I cant just edit them in place, and doing so just recreates them each time.
# May as well conver them to lists, mod them, then compare them. Or I guess go
# ahead and recreate them in place each time at the expense of cycles.
# I dont think you can get a 100 for both mem and time in one, its a tradeoff


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        #         s_list = [list(s)]
        #         t_list = list(t)

        #         i = 0
        #         while s_list and i < len(s_list):
        #             if s_list[0] == "#":
        #                 s_list = s_list[1:]
        #                 continue
        #             if s_list[i] == "#":
        #                 s_list = s_list[: i - 1] + (s_list[i + 1 :] if i < len(s_list) - 1 else [])
        #                 i -= 2
        #             i += 1

        #         i = 0
        #         while t_list and i < len(t_list):
        #             if t_list[0] == "#":
        #                 t_list = t_list[1:]
        #                 continue
        #             if t_list[i] == "#":
        #                 t_list = t_list[: i - 1] + (t_list[i + 1 :] if i < len(t_list) - 1 else [])
        #                 i -= 2
        #             i += 1
        #         return s_list == t_list

        # Im an idiot, this is exactly what stacks are for

        s_list = []
        t_list = []

        for c in s:
            if c == "#":
                if s_list:
                    s_list.pop()
            else:
                s_list.append(c)
        for c in t:
            if c == "#":
                if t_list:
                    t_list.pop()
            else:
                t_list.append(c)

        return s_list == t_list
