1011. Capacity To Ship Packages Within D Days
#knapsack problem

#So to deliver n packages in d days, you need to process at least
# ceil(n/d) on SOME days. 20 package in 6 days means you have to spend
# at least 2 days sending 4 packages. So thats actually 
# n%d days of sending ceil(n/d) packages + 
# d- n%d days of sending floor(n/d) packages

#oh... whew. The cargo MUST be shipped in the order given. Was worried about
#having to somehow optimize distribution. 



# class Solution:
#     def shipWithinDays(self, weights: List[int], days: int) -> int:
class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        # Set the range of possible weight capacities
        left = max(weights)
        right = sum(weights)
        
        while left < right:
            mid = (left+right) // 2
            day_count = 1
            total_weight = 0
            
            for weight in weights:
                total_weight += weight
                
                if total_weight > mid:
                    day_count += 1
                    total_weight = weight
            
            if day_count > D:
                left = mid + 1
            else:
                right = mid
        
        return left