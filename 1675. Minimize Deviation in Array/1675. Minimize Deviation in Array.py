#Ok, so the reason to use a heap is that you ALWAYS want to be testing the max val
#in your remaining list. You might get to what you think is the last value to test
#and it turns out its even and can be divided by 2 and is suddenly your NEW
#minimum value: now theres a bunch of intermediates that need to be retested.
#You need to keep reiterating until the max value (after having"maximized' the odds)
# IS odd, and thus cannot be reduced further. 

nums = [10,4,3]

#increase all the odds. Therefore the only possible option is reducing
for i in range(len(nums)):
    if nums[i]%2==1:
        nums[i] *= 2

nums.sort()
nums_max = nums[-1]
nums_min = nums[0]
        
for i in range(len(nums)-1, 1, -1)



# #BAH! Attempt two was close but again, it pretty hard to determine the target value. 

# nums = [10,4,3]
# nums.sort()
# for x in nums:
#     if x % 2 == 0:
#         min_even = x
#         break

# for i in range(len(nums)):
#     while nums[i] % 2 == 0 and nums[i]//2 > nums_min:
#         nums[i] = nums[i] // 2

# nums_max = max(nums)

# for i in range(len(nums)):
#     if nums[i] % 2 == 1:
#         if nums[i] < nums_min:
#             nums_min = nums[i]
#         if (abs((nums[i] * 2) - nums_max)) < abs((nums[i] - nums_max)):
#             if (nums[i] * 2 <= nums_max) or nums[i] == nums_min: 
#                 if nums[i] == nums_min:
#                     nums_min = nums[i]*2
#                 nums[i] *= 2
#             if nums[i] > nums_max:
#                 nums_max = nums[i]

# dev = abs(nums_max - nums_min)
# print(dev)

# nums = [
#     2,
#     8,
#     10,
# ]
# evens = []
# odds = []
# min_even = 10 ** 9 + 2
# max_even = -2
# min_odd = 10 ** 9 + 1
# max_odd = -1

# for x in nums:
#     if x % 2 == 0:
#         evens.append(x)
#     else:
#         odds.append(x)

# odds.sort()
# evens.sort()
# if len(evens) - 1 > 0:
#     max_even = evens[len(evens) - 1]
# else:
#     []
# if len(evens) > 0:
#     min_even = evens[0]
# else:
#     []
# if len(odds) - 1 > 0:
#     max_odd = odds[len(odds) - 1]
# else:
#     []
# if len(odds) > 0:
#     min_odd = odds[0]
# else:
#     []

# for x in range(len(evens)):
#     while evens[x] % 2 == 0 and abs((evens[x] // 2) - max_odd) <= abs(
#         evens[x] - max_odd
#     ):
#         evens[x] = evens[x] // 2
# max_even = max(evens)

# for x in range(len(odds)):
#     if (
#         abs((odds[x] * 2) - max_odd) < abs((odds[x] - max_odd))
#         and (odds[x] * 2) <= max_even
#     ):
#         odds[x] = odds[x] * 2

# new_max = max(max(evens), max(odds))
# new_min = min(min(evens), min(odds))
# min_dev = abs(new_max - new_min)

# print(min_dev)



# AT PRESENT THIS IGNORES, OR WORSE, REQUIRES THERE BE AT LEAST ONE EVEN AND ONE ODD NUMBER
# Ok, ive broken the logic on this by not seperating out the operations enough. I had the
# right sort of idea: Evens can decrease, odds can only increase once. I got stuck
# trying to identify a target FIRST than move things toward the target, but realized
# the target may be moving, and determining it in the first place is difficult and
# leaves out all sorts of obvious edge cases (all evens for instance).

# Trying again by reducing all values to their minimum FIRST. This automactically
# moves us towards a smaller deviation, AND makes ALL NUMBERS IN THIS SET ODD
# The MAX of this new set will then just be the largest ODD number and should
# DEFINITELY be the target. We then simply check if doubling each number in the set
# decreases this deviation. We only need to check each number once as odds can only
# # toggle between doubling/halving one step.


# ugh, fine. Lets look at enumerate for this loop instead of for range len
# Nope, I hate it. when returning the tuple i, x for enumerate(list),
# the x value is merely a copy, so you cannot edit it directly for recomparison
# in the loop. You have to resort to modifying list[i] anyhow, so x is only useful
# if you are treating the list as immutable
