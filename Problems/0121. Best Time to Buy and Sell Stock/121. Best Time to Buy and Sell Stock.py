prices = [7, 1, 5, 3, 6, 4]

best_low_i, next_low_i = 0, 0
best_profit = 0

for price in range(1, len(prices)):
    if prices[price] < prices[next_low_i]:
        next_low_i = price
        # if a lower price is found store it to see if it may result in a higher profit
    if prices[price] - prices[next_low_i] > best_profit:
        # if at some point our potential latest low price is proved to sell at a higher proft margin
        # update the index of the new best price, and related best profit given the curr high
        # implicityly cathces first case of profit as init has best_low_i = next_low_i
        best_low_i = next_low_i
        best_profit = prices[price] - prices[best_low_i]

print(best_profit)

# as suspected, the following was too time costly, O(n**2) as the forward look for better profit
# might involve iterating through the rest of the list each time.
# No need! we only need to see if the curr iteration changes the profit margin for the better
# and if so, update either the low or the high, whichever improves


# for i in range(1, len(prices)):
#     if prices[i] <= prices[low_idx] and max(prices[i:]) - prices[i] >= curr_profit:
#         # if we find a new, lower price AND we can sell this at price in the future for greater
#         # than our current profit margin... (Note, this makes the op O(N**2) worst case...)
#         low_idx = i
#         high_idx = i                            #we know this will get set to some future max identified above.
#                                                 #We dont want have to search a second time, the loop will find it
#     if prices[i] > prices[high_idx]:
#         high_idx = i
#     curr_profit = prices[high_idx] - prices[low_idx]

# print(curr_profit)
