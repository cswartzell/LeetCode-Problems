# class Solution:
#     def __init__(self):
#         self.coinlist = []
#         self.max_amount = 0

#     def coinChange(self, coins: List[int], amount: int) -> int:
#         # AAAAAAAND scratch all that. I realized that I was essenntially performing
#         # a depth first search, but this does not lend itself well to memoization
#         # which I knew was going to be the key to efficiency. Instead we want to do
#         # a breadth first search, selecting one of each coin as the next coin, and
#         # calculating the remaining amount. Eventually if we reach zero on a path
#         # we can backtrack levels and save at each level the minimum number of coins
#         # to get to that sub-sum. Memoizing this, eventually we will have to do less
#         # and less work. Can we use the memoize decorator to do this automatically?
#         # Lets see.

#         # ALWAYS think of the trivial base cases...
#         if amount == 0:
#             return 0

#         self.max_amount = amount

#         # Toss any too large coins, sort the remainder
#         self.coinlist = sorted((x for x in coins if x <= amount), reverse=True)
#         # Are there even any coins left?
#         if not coins:
#             return -1

#         # @cache could not hash passing coins. As coins isnt changing
#         # why bother passing it each time. Part of a class, could
#         # be protected and thus accessed by this class method?
#         @cache
#         def coinDrill(amount) -> int:
#             if amount == 0:
#                 return 1
#             bits = self.max_amount
#             for x in self.coinlist:
#                 bits = min(bits, coinDrill(amount - x))
#                 if bits == 1:
#                     return bits + 1
#             return -1

#         total_coins = coinDrill(amount)
#         return total_coins if total_coins >= 0 else -1


# # Ok, Im going on an adventure in 'advanced' python here. Yes, I can
# work on coding this from scratch and should do so after this, before
# consulting the solution. For now, this is an LCM problem, and I'd like to
# explore (probably numpy) libraries for use of that function, if its efficient.
# For each multiple of the largest remaining coin.... No wait, this doesnt work either
# We can't just start with the largest coin. Hell [296, 150, 1] amount 300 would be
# ONLY two of the 150 coins, ignoring the largest coin... Ok... any coins that are
# MULTIPLES of a smaller coin (and less than remaining_amount) should be automatically
# considered? Even then, no... same reason ([296,150, 148,1]). I think we may genuinely
# have to generate every combination, or at least all of those that potentially have
# fewer coins than our current record as we go...

#         #ALWAYS think of the trivial base cases...
#         if amount == 0: return 0

#         #Toss any too large coins, sort the remainder
#         coins = sorted((x for x in coins if x <= amount), reverse=True)

#         #Are there even any coins left?
#         if not coins:
#             return -1

#         def coinDrill(coins,amount) -> int:
#             bits = 0
#             denomination = coins[0]
#             for x in range(amount//denomination, -1, -1):
#                 if amount - (x * denomination) == 0:
#                     return x
#                 elif len(coins) == 1:
#                     return 0
#                 else:
#                     bits = x + coinDrill(coins[1:], amount - (x * denomination))
#                     if bits > x:
#                         break
#             return bits

#         total_coins = coinDrill(coins,amount)
#         return total_coins if total_coins > 0 else -1


# AHA! Ok, that's the reason its a medium. I was wondering as this seemed
# to be pretty trivial, but I was imagining the scenario of US coins, which
# notably all have an LCM of the smallest coin, so you can always make change
# by starting with the largest and working your way down. With arbitrary values
# this is not the case: Giving X number of largest coins first might completely
# preclude making change at all.

#         #ALWAYS think of the trivial base cases...
#         if amount == 0: return 0

#         coin_count = 0
#         coins.sort(reverse=True)

#         for denomination in coins:
#             if amount >= denomination:
#                 coin_count += amount // denomination
#                 amount -= (amount // denomination)*denomination
#                 # While this looks foolish, this cant cancel as its INT division
#                 if amount == 0: return coin_count

#         return -1
