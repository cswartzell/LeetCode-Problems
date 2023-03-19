# Well, immediately I see two was to handle this. Kind of 3.
# The trivial one to implement is to simply store a hashmap, like a set.
# We could go a bit more advanced and roll our own hash, disucuss the merits
# and intricacies in selecting a hashing algo, colisions etc.

# Or we can make a Trie. Trie is most compact and "fancy", plus memory
# efficient. Because we include wild card chars trie makes this simpler


# class WordDictionary:
#     def __init__(self):
#         self.words = dict()
#         self.final = False

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

import re
import string

class WordDictionary:
    def __init__(self):
        self.words = set()
    
    def addWord(self, word: str) -> None:
        self.words.add(word)

    def search(self, word: str) -> bool:
        if word in self.words:
            return True
        #Pretty sure I am being EXTRA here. Can just use the dot notation DIRECTLY for a regex search
        #This matches valid words, but we didnt put any such restricions on the words in the first place
        # regx = "".join(ltr if ltr in string.ascii_letters else "[a-zA-Z]" for ltr in word)
        re_word = re.compile("\A"+word+"$")
        return re.search(re_word, s_word) for s_word in self.words



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

wordD = WordDictionary()
wordD.addWord("dad")
wordD.addWord("bad")
wordD.addWord("mad")
print(wordD.search("pad"))
print(wordD.search("bad"))
print(wordD.search(".ad"))
print(wordD.search("b.."))
