# 07-07-2023 Leetcode 0316. Remove Duplicate Letters
# https://leetcode.com/problems/remove-duplicate-letters/description/

# Count number of each letter (frequency map)
# Oh right, stacks exist.

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        in_stack = set()
        letter_count = collections.Counter(s)

        for i in range(len(s)):
            if s[i] in in_stack:
                letter_count[s[i]] -= 1
            else:
                while stack and stack[-1] > s[i] and letter_count[stack[-1]] > 0:
                    removed = stack.pop()
                    in_stack.remove(removed)
                stack.append(s[i])
                letter_count[s[i]] -= 1
                in_stack.add(s[i])
            
        return "".join(stack)