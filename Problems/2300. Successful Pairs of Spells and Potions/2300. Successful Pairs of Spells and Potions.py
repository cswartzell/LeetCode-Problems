# 04-01-2023 2300. Successful Pairs of Spells and Potions
# https://leetcode.com/problems/successful-pairs-of-spells-and-potions/description/

# Sort potions and binary search for the minimum powered potion to match the given spell.
# You'll have the index of the minimum potion, thus every one to the right also pairs, so
# its just len(potions) - min_potion_idx.

# I always wonder about an abstract data type that stores some metadata about a sorted array,
# like... why bother binary searching it over and over, we LEARN some stuff each time we search it
# we could keep a very small sample table, say 8 indexes that might give us some range info and
# thus cut down on our search space


class Solution:
    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        potions.sort()
        # pot_len = len(potions)
        # pairs = []
        # for spell in spells:
        #     min_pot = bisect.bisect_left(potions, success / spell)
        #     pairs.append(max(pot_len - min_pot, 0))

        # return pairs

        # spells.sort()
        return [
            len(potions) - bisect.bisect_left(potions, success / spell)
            for spell in spells
        ]
        return [
            len(potions)
            - bisect.bisect_left(potions, success, key=lambda potion: potion * spell)
            for spell in spells
        ]
        # return [len(potions) - bisect.bisect_left((pots := sorted(potions)), success/spell) for spell in spells]
