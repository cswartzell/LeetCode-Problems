# 03-28-2023 leetcode 1402. Reducing Dishes
# https://leetcode.com/problems/reducing-dishes/description/


# First, you dont want to dump ALL the negatives, just if their inclusion does more harm than good
# This is probably the hard part.
# Secondly, once you have removed negatives, you DEFINITELY want to prepare them in worst to best
# order. That way the negatives or low dont waste high multipliers. So thats just sort and andd.

# So the ONLY issue is what negatives to dismiss. 
# Start by sorting. Then compute the sum of products in the non-negative portion.
# Ok, so for each negative number, you add the sum of the non-negs to your total again, 
# subtract the sum of the current negatives, then subtract the new negative and ADD it
# to the current negatives total. As long as the total keeps going, include the new negative.
# We only need to maintain the max, not the order or which dishes we use. This doesnt seem that hard.


#I have to say, I am extremely please with this. Broke out bisect, enumerate in a generator, negative
# slicing. All sorts of fun basic tricks. What a neat problem. 


# The Missing Test Cases: 
# Medium with negatives: [-1,-8,0,5,-9]. Correct Answer: 14
# Long: 

class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        last_neg = bisect.bisect_left(satisfaction,0)
        positive_ltc_sum = sum(satisfaction[last_neg:])
        negative_ltc_sum = 0
        max_ltc = sum((multiplier + 1) * score for multiplier, score in enumerate(satisfaction[last_neg:]))

        if last_neg:
            for new_low in satisfaction[last_neg-1::-1]:
                if (new_ltc := max_ltc + positive_ltc_sum + negative_ltc_sum + new_low) > max_ltc:
                    max_ltc = new_ltc
                    negative_ltc_sum += new_low
                else:
                    break
        return max_ltc
