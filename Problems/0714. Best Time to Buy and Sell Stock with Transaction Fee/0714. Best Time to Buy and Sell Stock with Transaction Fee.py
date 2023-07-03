# 06-21-2023 Leetcode 714. Best Time to Buy and Sell Stock with Transaction Fee
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/description/


# Ok, I dont know the trick. I could of course do a "take it or leave it"
# recursive solution, but thats obviously going to fail as the len of days
# is up to 50,000. So we need a DP solution, not a plain recusrive.

# We could perhaps exit early if we keep a DP and discover on a given day
# we are in some set state (does NOT have stock) and if we dont currently have 
# at least as much as the max profit seen so far terminate. Cant beat the leader
# if we are already behind. 

# Wasnt the base problem more like a two pointer? "Last best point to buy in"
# and update that as prices go monotonically down. "Best sell date" as prices
# monotonically go up? so 1, 3, 5, 3, 10 would buy at 1 sell at 5 buy at 3, 
# sell at 10. We strictly want to sell IMMEDIATELY at the highest price. If it
# comes down, then goes even further we can just buhy again and sell at the higher
# price getting MORE profit as we double the value of the dip. 

# In this case you DONT want to sell immediately as it will cost you to sell,
# and AGAIN to buy back it. I think we want to sell at the last high if we 
# dip TWICE the fee in value as there is no point hanging on if it goes up:
# we could just buy on this day (value = recent max - 2xfee) and be in the 
# same position. 

#Cases:
# Have NO stock:
# Note the lowest prcice. Keep moving as price drops. No sense buying early
# No other cases. Only looking for low point to buy in, and just noting its index
# We mark the stock as "bought" but we dont subtract its cost or fee til selling,
# its a phantom buy. We wont carry it out if there is no profit, and thats 
# calculated in has_stock cases:

# Have stock:
# If the price goes up, great. Mark as new high and continue. 
# If the price goes down, but not less than the fee or currently profiable, continue. 
#   MAYBE we will see better prices. We cant earn EXTRA profit by bailing early yet

# If the price is BELOW what we bought in at, switch to this new price?***

# If the price goes down TWICE the fee, we are losing money. Sell at last high.
#    ASSUMING THERE WAS ANY PROFIT AT ALL> if not, ignore this whole round
#    Now go back in time to this day, and the next day we will NOT have stock
#    and can continue checking from there

#We may be left with stock in the end as this algorithm ONLY sells after a bad dip
# We need to run the sales check one last time if we have stock to sell at the last
# profit point. 


#Replace buy_price with last_low? Doesnt look like I need it afterall

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # Ridiculous looking amazing brief answer
        # hold, free = -prices[0], 0
        
        # for i in range(1, len(prices)):
        #     hold, free = max(hold, free - prices[i]), max(free, hold + prices[i] - fee)
        
        # return free

        last_low = 0
        last_high = 0

        total_profit = 0
        curr = 1
        
        while curr < len(prices):
            # Value only increasing. Note new high and continue
            if prices[curr] >= prices[last_high]:
                last_high = curr
                
            # Value dips below high less fee, we should have sold ASSUMING profit OR NEVER BOUGHT
            elif prices[curr] < prices[last_high] - fee:
                if prices[last_high] - prices[last_low] - fee > 0:  
                    total_profit += prices[last_high] - prices[last_low] - fee

                last_high = curr
                last_low = curr
            # Otherwise, its a minor dip. Keep theoreically holding? 
           
            #New low, restart tracking (if it would have caused a sale, thats handled by above)
            elif prices[curr] <= prices[last_low]: 
                last_low = curr
                last_high = curr
          
            curr += 1
        
        if prices[last_high] - prices[last_low] - fee> 0:  
            total_profit += prices[last_high] - prices[last_low] - fee

        return total_profit

        # last_low = 0
        # last_high = 0

        # total_profit = 0
        # curr_profit = 0
        # curr = 1
        
        # while curr < len(prices):
        #     # Value only increasing. Note new high and continue
        #     if prices[curr] >= prices[last_high]:
        #         last_high = curr
        #         curr_profit = prices[last_high] - prices[last_low]  - fee


        #     # Value dips below high less fee, we should have sold ASSUMING profit OR NEVER BOUGHT
        #     elif prices[curr] < prices[last_high] - fee:
        #         if curr_profit > 0:  
        #             total_profit += curr_profit

        #         curr_profit = 0    
        #         last_high = curr
        #         last_low = curr
        #     # Otherwise, its a minor dip. Keep theoreically holding? 
           
        #     #New low, restart tracking (if it would have caused a sale, thats handled by above)
        #     elif prices[curr] <= prices[last_low]: 
        #         last_low = curr
        #         last_high = curr
          
        #     curr += 1

        # if curr_profit > 0:  
        #     total_profit += curr_profit
        
        # return total_profit

# class Solution:
#     def maxProfit(self, prices: List[int], fee: int) -> int:
#         last_low = 0
#         last_high = 0

#         profit = 0
#         has_stock = False
#         buy_price = 0
#         curr = 1
        
#         while curr < len(prices):
#             if has_stock:
#                 # Value only increasing. Continue
#                 if prices[curr] >= prices[last_high]:
#                     last_high = curr

#                 # Prices went down slow after buying so we buy later
#                 elif prices[curr] < buy_price:
#                     buy_price = prices[curr]
                
#                 # Value dips below high less fee, we should have sold ASSUMING profit OR NEVER BOUGHT
#                 elif prices[last_high] - fee >= prices[curr]:
                
#                     if prices[last_high] - buy_price - fee > 0:  
#                         profit += prices[last_high] - buy_price - fee
                        
#                     #Go back to the point we just sold at and continue as we DONT have stock? 
#                     last_high += 1
#                     last_low = last_high
#                     curr = last_high
#                     has_stock = False
#                     buy_price = 0
               
#                 # Otherwise, its a minor dip. Keep theoreically holding? 
            
#             else:
#                 # Better price available, mark and continue
#                 if prices[curr] < prices[last_low]:
#                     last_low = curr
#                 # Price is increasing, mark as POTENTIALLY bought
#                 else:
#                     has_stock = True
#                     buy_price = prices[last_low]
#                     last_high = curr
#             curr += 1

#         if has_stock:
#             if prices[last_high] - buy_price - fee > 0:
#                 profit += prices[last_high] - buy_price - fee
                    
#         return profit

1