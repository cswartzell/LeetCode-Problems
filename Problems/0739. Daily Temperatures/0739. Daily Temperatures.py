# 11-27-2022 LeetCode 739. Daily Temperatures
# https://leetcode.com/problems/daily-temperatures/description/

# Hey look, I did a monotonic stack thing! Definitely a new concept and
# pattern for me, I'll need to do a few more to really get it to click
# as a usable solution. This one is a very good beginer exercise for
# learning them, as their application here is pretty clear

# Look the ith temperature. Is there anything on the stacK? If no, then
# this cant be higher than anything previous. On the stack it goes.
# If there is an item on the stack, then is this colder (or the same)?
# If so, its colder than everything on the stack and when need to keep looking.
# On the stack it goes. Note, here I added tuples of the data itself and then
# later realized I actuall;y needed the index too, as the things on the stack,
# while still in order, have gaps. Their positioning infor will be lost otherwise
# If I had thought about it, I would have realized I DONT actually need to store
# the data itself on the stack, if I have the index I can just pull that out
# of the original list. Anyhow, now we have a stack of cold days.
# Our next days turns out to be hot. We check ONLY the top of the stack, as
# we know thats the coldest so far (its monotonically decreasing after all);
# If this new days temp is warmer, we pop the position data off the stack and
# use the difference (1 day) to be stored in the answer array at the same index
# as the stored index in our monostack. We then repeat this for each element
# in the monostack, does our ith day beat the next coldest day?
# We either exhaust the stack, or find a day that ISNT colder than the ith day.
# Note we need to peek the stack, or pop and push for languages where thats
# not possible. Lastly, we dont know what the status of tomorrow is, so we
# put the ith day itself on the stack. As we initialized our array to all
# 0, at the end maybe we have some days on the stack that never got updated,
# but the ans list will have the default/sentinel value already stored. This
# also automatically handles the final day.

# It may be good in an interview to ask about how to handle the final day.
# We are told explicitly to return 0 for days that have no subsequent
# hotter day within the week, but does that necessarily cover the final day?
# What if we should instad return an array thats one day shorter? This seems
# like the logical answer, but asking for clairty may be good. You wouldnt
# want side effects for just assuming this default value.


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0 for _ in range(len(temperatures))]

        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                ans[stack[-1][1]] = i - stack[-1][1]
                stack.pop()
            stack.append((temperatures[i], i))

        return ans
