# 02-02-2023 Leetcode 953. Verifying an Alien Dictionary
# https://leetcode.com/problems/verifying-an-alien-dictionary/description/


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        lex_order = {index: letter for letter, index in enumerate(order)}

        # Find the len of the longest word, and terminate early if the words arent in
        # equal/increasing length order
        # len_max_word = 0
        # for i in range(1, len(words)):
        #     if len(words[i]) < len(words[i-1]):
        #         return False
        #     len_max_word = max( len(words[i]), len_max_word)

        # For each (pair) of words, starting at second:
        for word_idx in range(1, len(words)):
            # for each letter position in the words
            for letr_idx in range(len(words[word_idx - 1])):
                # If the second word is shorter than the first (AND all previous letters matched, implicitly)
                # OR if the score of the letter in the second letter is LOWER than that of the first, return False
                if (
                    len(words[word_idx]) - 1 < letr_idx
                    or lex_order[words[word_idx][letr_idx]]
                    < lex_order[words[word_idx - 1][letr_idx]]
                ):
                    return False
                # If there WAS a letter in both, and the letter in the second word is greater, the order is preserved and we can break early
                elif (
                    lex_order[words[word_idx][letr_idx]]
                    > lex_order[words[word_idx - 1][letr_idx]]
                ):
                    break

        return True

        # Im an idiot. You dont need to check each letter.
        # You only continue to check letters IFF the proceeding letters are tied
        # Checking further letters is merely a tie breaker.
        # im dum

        # for letter_idx in range(len_max_word-1,-1,-1):
        #     for word_idx in range(len(words)-1,0,-1):
        #         #If the proceeding word doesnt have a letter at this idx (is shorter), restart
        #         if len(words[word_idx-1]) - 1 < letter_idx:
        #             break
        #         prev_word_letter_score = lex_order[words[word_idx-1][letter_idx]]
        #         curr_word_letter_score = lex_order[words[word_idx][letter_idx]]
        #         if lex_order[words[word_idx-1][letter_idx]] > lex_order[words[word_idx][letter_idx]]:
        #             return False
        # return True
