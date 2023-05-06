# 03-18-2023 Leetcode 211. Design Add and Search Words Data Structure
# https://leetcode.com/problems/design-add-and-search-words-data-structure/description/

# Well, immediately I see two was to handle this. Kind of 3.
#We COULD store a simple set and for any '.' in a word, we add
#all 26 possible vals to our set. There can be up to 3 dots however
#and 26^3 = 17576 possible words in a three dot word. Our set will be
# too big. 

#We can use REGEX to simply match within a set, this is trivial too.

#Or we can make a Trie. Trie is most compact and "fancy", plus memory
#efficient.

#Lets go for trie for the practice:
# Hooray! Worked first try. Slow as shit, barely passing
 
# class WordDictionary:
#     def __init__(self):
#         self.words = dict()
#         self.final = False
#         self.longest = 0

#     def addWord(self, word: str) -> None:
#         if not word:
#             self.final = True
#             return
#         if word[0] not in self.words:
#             self.words[word[0]] = WordDictionary()
#         self.words[word[0]].addWord(word[1:])
            
#     def search(self, word: str) -> bool:
#         if not word:
#             return self.final
#         if word[0] in self.words:
#             return self.words[word[0]].search(word[1:])
#         elif word[0] == ".":
#             return any(self.words[wordD].search(word[1:]) for wordD in self.words)
#         else:
#             return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)



# # # REGEX
# import re

# class WordDictionary:
#     def __init__(self):
#         self.words = collections.defaultdict(set)
    
#     def addWord(self, word: str) -> None:
#         self.words[len(word)].add(word)

#     def search(self, word: str) -> bool:
#         if word in self.words[len(word)]:
#             return True 
#         return any(re.search(word, match) for match in self.words[len(word)])


