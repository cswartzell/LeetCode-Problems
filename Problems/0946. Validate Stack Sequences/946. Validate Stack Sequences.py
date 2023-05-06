"""03-16-2022 LeetCode 946. Validate Stack Sequences"""
import queue


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        if not pushed or not popped:
            return False
        popped.reverse()
        pushed.reverse()
        # ugh. O(n), but it beats popping from the head each time O(n**2)
        # I could just try setting a negative val as a flag and skipping...
        stackyboi = []

        curr = popped.pop()

        while pushed or popped or stackyboi:
            if pushed == [] and stackyboi[-1] != curr:
                return False
            if pushed:
                if pushed[-1] == curr:
                    pushed.pop()
                    if popped:
                        curr = popped.pop()
                    continue
            if stackyboi:
                if stackyboi[-1] == curr:
                    stackyboi.pop()
                    if popped:
                        curr = popped.pop()
                    continue
            if pushed:
                stackyboi.append(pushed.pop())

        # if stackyboi == pushed == popped == []:
        #     return True
        return True
