"""2/13/2022 LeetCode 127. Word Ladder"""
import re
from collections import defaultdict

# class Solution:
#     def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

wordList = ["hot", "dot", "tog", "cog"]
beginWord = "hit"
endWord = "cog"

if endWord not in wordList:
    print(0)
# str_str = " ".join(wordList)

graph_dict = defaultdict(list)

for word in wordList:
    for i in range(len(word)):
        pattern = word[0:i] + "[a-z]" + word[i + 1 :]
        # graph_dict[pattern] = re.findall(pattern, str_str) #while fun to match using RE, this is doing the same work over and over
        graph_dict[pattern].append(word)

ladder_dict = {0: set([beginWord])}
depth = 0
visited_set = set()

while True:
    depth += 1
    ladder_dict[depth] = set()
    for next_word in ladder_dict.get(depth - 1):
        if next_word not in visited_set:
            for j in range(len(next_word)):
                pattern = next_word[0:j] + "[a-z]" + next_word[j + 1 :]
                tmp_set = ladder_dict[depth]
                tmp_set.update(graph_dict.get(pattern, []))
                if endWord in ladder_dict.get(depth):
                    print(depth + 1)
    visited_set.update(ladder_dict[depth - 1])
    ladder_dict[depth] -= visited_set
    if ladder_dict[depth] == set():
        break
print(0)
