# 02-04-2023 Leetcode 438. Find All Anagrams in a String
# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/

# this is admittedly perhaps overly verbose. This was more an exercise in reusing
# and adapting existing code: The previous day's excercise was exactly this, but
# only returning true once we found ONE match, not the index of the start of every
# match. Pretty minor editing to get this 96%+ code working. Looks a mess though.
# 567. Permutation in String


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        p_counter = collections.defaultdict()
        p_counter.update(collections.Counter(p))
        temp_counter = collections.defaultdict(int)
        curr_queue = collections.deque()
        anagram_i_start = list()
        curr_start_i = None

        for i in range(len(s)):
            if curr_start_i == None:
                curr_start_i = i
            if s[i] in p_counter:
                while temp_counter[s[i]] >= p_counter[s[i]]:
                    temp = None
                    while temp != s[i]:
                        curr_start_i += 1
                        temp = curr_queue.popleft()
                        # temp_counter[temp] = min(0, s1_counter[temp] - 1)
                        temp_counter[temp] -= 1
                        if temp_counter[temp] == 0:
                            del temp_counter[temp]
                temp_counter[s[i]] += 1
                curr_queue.append(s[i])
            else:
                temp_counter.clear()
                curr_queue.clear()
                curr_start_i = None
            if temp_counter == p_counter:
                anagram_i_start.append(curr_start_i)

        return anagram_i_start
