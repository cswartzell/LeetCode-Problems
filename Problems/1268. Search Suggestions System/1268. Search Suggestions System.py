# 03-13-2023 Leetcode 1268. Search Suggestions System
# https://leetcode.com/problems/search-suggestions-system/description/

# Is this a Trie Problem? I think it might be.
# lets try list and sliding window first

# Ok, that works. Now: How dumb is it?
# We could do a complicated tree, but how about instead we just marginally improve
# this to a reasonable degree: we can make a dict of products using only the first
# letter. This massively reduces the list after the first letter is typed. Not quite
# to 1/26 for any real world named items, but WOULD work for alphakeyed random names
# At this point we COULD then make a dict of items for the every second letter as the value
# for the first dict entry. Now suddenly we have 26**2 dicts. We could then keep doing this
# for each letter in every product til the product is fully placed in this web of dicts...
# but it seems like generating that in the first place would be costly.

# if this was enterprise software, maybe it makes sense to keep such a dict globally sorted
# and update date it over time: not the case here. We are given an unordered list and have to
# determine whats worth our time.

# The ADVANTAGE of a TRIE method is that it is reversible.


# Oh goddamnit. Just binary search the current slice, then iterate from there to pickup the first
# list.

# class Solution:
# def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
# Yes, I could destructively reduce the list, but as lists are pass by ref,
# this seems like bad practice. I dont know if can destroy the list, so I shouldnt
# its only 1000 strs of len 3000, whats 3 million characters? A few KB
# products_temp = sorted(products)

# suggestions = []
# product_match_range_start = 0
# product_match_range_end = len(products_temp) - 1

# for i in range(1,len(searchWord)+1):
#     curr_suggest = []
#     j = 0
#     while products_temp and len(curr_suggest) < 3 and j < len(products_temp):
#         if searchWord[:i] == products_temp[j][0:i]:
#             curr_suggest.append(products_temp[j])
#             j += 1
#         else:
#             del products_temp[j]

#     suggestions.append(curr_suggest)
# return suggestions


# This allows us to theoretically backtrack as its not destructive.
# User could hit backspace and we could recover.
# Heck, we could store an array of position starts per letter, and
# merely pop the last element off the array and we'd have the previous
# position start. Could even store the suggestion at that point as part of
# a tuple and then we wouldnt even need to rerun the last. Wed have the complete
# previous result. This seems like a worthy tradeoff for the very little memory it takes


# products_temp = sorted(products)


# suggestions = []
# product_match_range_start = 0
# # product_match_range_end = len(products_temp)
# next_product_match_range_start = 0

# for i in range(1,len(searchWord)+1):
#     curr_suggest = []
#     j = 0
#     # next_product_match_range_start = product_match_range_start
#     while len(curr_suggest) < 3 and product_match_range_start + j < len(products):
#         if searchWord[:i] == products_temp[product_match_range_start + j][0:i]:
#             curr_suggest.append(products_temp[product_match_range_start + j])
#         elif curr_suggest:
#              break
#         else:
#             next_product_match_range_start += 1
#         j += 1

#     suggestions.append(curr_suggest)
#     product_match_range_start = next_product_match_range_start

# return suggestions


####################################################################################################################
# Trie Version: DEFO had to look at someone elses code to get this, but handy to try it blind after
class Solution:
    def suggestedProducts(
        self, products: List[str], searchWord: str
    ) -> List[List[str]]:
        # Define a TrieNode: Has a dict of other trieNodes it points to.
        class TrieNode:
            def __init__(self):
                self.children = collections.defaultdict(TrieNode)
                self.suggestions = []

            def add_sugestion(self, suggestion):
                if len(self.suggestions) < 3:
                    self.suggestions.append(suggestion)

        products.sort()

        # Create the Trie Root
        root = TrieNode()
        # Build up Tree: For each letter, in each word, get to the next trie node, and append the word to it
        # As we are only adding the first three words for each prefix, and they are ALREADY sorted,
        # we know we will store the first 3 matches, in order
        for word in products:
            curr_node = root
            for letter in word:
                curr_node = curr_node.children[letter]
                curr_node.add_sugestion(word)

        # Parse input, return suggestions, only need to move current node along one letter at a time in order
        # to go deeper and deeper into the trie. EACH trie has all (up to) 3 matches for the given prefix, so
        # simply return it.
        ans = []
        curr_node = root
        for letter in searchWord:
            curr_node = curr_node.children[letter]
            ans.append(curr_node.suggestions)

        return ans
