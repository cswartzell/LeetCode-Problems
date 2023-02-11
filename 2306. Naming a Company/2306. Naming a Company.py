# This seems overly simple. Maybe its easier to test all the cases
# that are INVALID and just subtract these from the maximum.

# The max number of combinations is of course n*(n-1), since using the same
# word twice is invalid. What are other invalid cases?

# remember that any valid pair is TWO possibilities as swapping within the
# pair will remain valid:

# Names would be invalid if they both started with the same letter:
# For every pair of same lettered words you lose two possibilities
# If we sort out words by their starting letter, we can check per letter how many
# total possiblities should be discounted by subtracting
# len(words_alpha[a])*(len(words_alpha[a])-1)

# Pairs are invalid if they share the same suffix after the first letter,
# as swapping their letters produces invalid words (eachother)
# Lack Back becomes Back LacK. which are already words
# THIS overlaps with the existing rule and may supercede it:
# if a word has its first letter replaced, and is still found to be a valid
# word, then all combinations (remember to double them) using that word with
# that letter are invalid.
# Again, using the words sorted into lists by first letter, we could reduce from
# our max combos the following:
# For each word, if replacing its first letter with LETR is another valid word,
# subtract 2*(len(words_alpha[LETR]))

# does that cover it?


# class Solution:
#     def distinctNames(self, ideas: List[str]) -> int:
class Solution:
    # max_combos = len(ideas) * (len(ideas)-1)
    # valid_pairs = max_combos
    valid_pairs = 0
    first_letters = collections.Counter([word[0] for word in ideas])

    # We'll be taking len(word) spins through letters in this lists
    # so this MAY be able to be added to that, but lets keep it seperate for clarity
    for letter in first_letters.keys():
        valid_pairs -= first_letters[letter] * (first_letters[letter] - 1)

    # Wait, is the above necessary? If so I need to ESCAPE removing the same letter
    # count here again, but maybe I can just use this as is and it will take of
    # the same counting? Which is more efficient? I think the above really

    # Shit, this double counts suffix similar words
    for word in ideas:
        for letter in first_letters.keys():
            if letter == word[0]:
                continue
            if letter + word[1:] in ideas:
                valid_pairs -= 2 * first_letters[letter]
                # corrects for double counting
                if letter < word[0]:
                    valid_pairs += 2

    return valid_pairs
