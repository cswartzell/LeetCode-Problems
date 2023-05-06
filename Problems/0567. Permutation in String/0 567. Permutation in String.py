# 02-04-2023 Leetcode 567. Permutation in String
# https://leetcode.com/problems/permutation-in-string/description/

# Sliding window with counter for contents as we are looking at permutations


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counter = collections.defaultdict()
        s1_counter.update(collections.Counter(s1))
        temp_counter = collections.defaultdict(int)
        curr_queue = collections.deque()

        for i in range(len(s2)):
            if s2[i] in s1_counter:
                while temp_counter[s2[i]] >= s1_counter[s2[i]]:
                    temp = None
                    while temp != s2[i]:
                        temp = curr_queue.popleft()
                        # temp_counter[temp] = min(0, s1_counter[temp] - 1)
                        temp_counter[temp] -= 1
                        if temp_counter[temp] == 0:
                            del temp_counter[temp]
                temp_counter[s2[i]] += 1
                curr_queue.append(s2[i])
            else:
                temp_counter.clear()
                curr_queue.clear()
            if temp_counter == s1_counter:
                return True

        return False
