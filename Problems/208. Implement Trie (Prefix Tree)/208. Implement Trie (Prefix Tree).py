# class Trie:
#     def __init__(self):
#         # self.Trie_dict = collections.defaultdict(Trie)
#         self.Trie_dict = dict()
#         self.words = set()

#     def insert(self, word: str) -> None:
#         # Wait, does a Trie have a copy of each word at EVERY level with a valid prefix of said word?
#         # That seems just inanely wasteful.

#         # if not word:
#         #     return
#         # if word[0] not in self.Trie_dict:
#         #     self.Trie_dict[word[0]] = Trie()
#         # self.Trie_dict[word[0]].insert(word[1:])

#         curr_trie = self
#         for letter in word:
#             if letter not in curr_trie.Trie_dict:
#                 curr_trie.Trie_dict[letter] = Trie()
#             curr_trie = curr_trie.Trie_dict[letter]
#             curr_trie.words.add(word)

#     def search(self, word: str) -> bool:
#         # if not word:
#         #     return True
#         # return word[0] in self.Trie_dict and self.Trie_dict[word[0]].search(word[1:])
#         if not word:
#             return False
#         return word in self.Trie_dict[word[0]].words

#     def startsWith(self, prefix: str) -> bool:
#         # could be lazy and just call search on the first letter, then the first two, then 3...
#         # curr_trie = self
#         # for letter in prefix:
#         #     if letter not in curr_trie.Trie_dict:
#         #         return False
#         #     curr_trie = curr_trie.Trie_dict[letter]
#         # return True

#         # Lol, the algorithm I wrote for search is wrong, but DOES work perfectly for prefix
#         # I forgot, you need to match the whole word AND stop.
#         # if not prefix:
#         #     return True
#         # return prefix[0] in self.Trie_dict and self.Trie_dict[prefix[0]].search(prefix[1:])

#         curr_trie = self
#         for letter in prefix:
#             if letter not in curr_trie.Trie_dict:
#                 return False
#             curr_trie = curr_trie.Trie_dict[letter]
#         return True


class Trie:
    def __init__(self):
        self.Trie_dict = dict()
        self.final = False

    def insert(self, word: str) -> None:
        curr_trie = self
        for letter in word:
            if letter not in curr_trie.Trie_dict:
                curr_trie.Trie_dict[letter] = Trie()
            curr_trie = curr_trie.Trie_dict[letter]
        curr_trie.final = True

    def search(self, word: str) -> bool:
        if not word:
            return False

        curr_trie = self
        for letter in word:
            if letter not in curr_trie.Trie_dict:
                return False
            curr_trie = curr_trie.Trie_dict[letter]
        return curr_trie.final

    def startsWith(self, prefix: str) -> bool:
        curr_trie = self
        for letter in prefix:
            if letter not in curr_trie.Trie_dict:
                return False
            curr_trie = curr_trie.Trie_dict[letter]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert("word")
# param_2 = obj.search("word")
# param_3 = obj.startsWith("wo")
# pass
results = []
test_trie = Trie()
results.append([])
test_trie.insert("apple")
param1 = test_trie.search("apple")
param2 = test_trie.search("app")
param3 = test_trie.startsWith("app")
test_trie.insert("app")
param5 = test_trie.search("app")
