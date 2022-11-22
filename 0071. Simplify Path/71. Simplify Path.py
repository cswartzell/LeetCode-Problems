"""03-12-2022 LeetCode 71. Simplify Path"""

import collections


path = "/../"


class Solution:
    def simplifyPath(self, path: str) -> str:
        path_stack = Deque()
        for x in path.split("/"):
            if x != "" and x != "." and x != "..":
                path_stack.append(x)
            if x == ".." and path_stack:
                path_stack.pop()

        return "/" + "/".join(path_stack)


#         subs = path.split("/")
#         x = 0
#         while x < len(subs):
#             if subs[x] == "" and x < len(subs):
#                 subs = subs[:x] + subs[x+1:]
#                 x -= 1
#             elif subs[x] == "." and x < len(subs):
#                 subs[x] = ""
#                 x -= 1
#             elif subs[x] == ".." and x < len(subs):
#                 subs = subs[:x] + subs[x+1:]
#                 if x != 0:
#                     subs = subs[:x-1] + subs[x:]
#                     x -= 1
#                 x -= 1
#             x += 1
#         return "/" + "/".join(subs)
