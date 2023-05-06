# 04-10-2023 Leetcode 71. Simplify Path
# https://leetcode.com/problems/simplify-path/description/

# Hmm... I guess I dont know these conventions as I am confused.
# What am doing with some of these? Clearly repeated slashes get compressed down.
# The fuck do I do with ".."? I guess simply delete it, or rather, it should ONLY
# exist as "/../" and I could just chop the last 3 chars? Similarly, "/./" -> "/"?

# Can I just get every thing after a "/" that isnt ".." or "." and join them with "/" betweeen?


class Solution:
    def simplifyPath(self, path: str) -> str:
        # canonical = ["/"]
        # i = 1 #absolute starts with / so we can ignore it

        elements = path.split("/")
        canonical_stack = []
        for element in elements:
            if element not in {"", ".", ".."}:
                canonical_stack.append(element)
            if element == ".." and canonical_stack:
                canonical_stack.pop()

        return "/" + "/".join(canonical_stack)
