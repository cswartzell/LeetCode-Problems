

# 01-03-2022 Leetcode 2244. Minimum Rounds to Complete All Tasks
# https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/description/

#isnt this just bucket sort and then ceil(task_i/3)?
#yep. Works fine, but slow. 

#We could keep a set for "seen once" so we dont have to scan
#through the val list. Or just iterate through the list instead
#of being lazy.

#Still slow? Ugh... we could keep a set for "seen first",
# then "multiple of 1, multiple of 2, multiple of 3" and cycle
# seen ints between them but that just seems silly.

#ugh. We could declare an array of task i size and set every i to say
# -2. On first seeing a number it gets added and becomes -1 (and if 
# this is the only one, this is correct). If a second instance is found
# the first -1 becomes positive 2. From there cycle 1,2, 0 (3), adding to
# rounds each time. Seems equally silly. Plus thats a big dumb array.
# Oh. could be a default dict, and then the default -2 happens naturally?


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:

        tasks.sort()

        rounds = 0
        curr_digit = 0
        curr_count = 0
        for x in tasks:
            if x != curr_digit:
                if curr_count == 1:
                    return -1
                rounds += (curr_count + 2) // 3
                curr_digit = x
                curr_count = 1
            else:
                curr_count += 1

        return rounds + (curr_count + 2) // 3

        #lol bottom 5%. 
        # task_counter = collections.Counter(tasks)
        # if 1 in task_counter.values():
        #     return -1
        # return sum([math.ceil(x/3) for x in task_counter.values()])


        #There it is
        # return max(sum(math.ceil(v/3) if v != 1 else -inf for v in Counter(tasks).values()), -1)

        #still bottom...
        # task_counter = collections.Counter(tasks)
        # rounds = 0
        # for x in task_counter.values():
        #     if x == 1:
        #         return -1
        #     rounds += math.ceil(x/3)
        # return rounds
        
        # THIS is better?!
        # rounds = 0
        # task_dict = collections.defaultdict(int)
        # for x in tasks:
        #     if x not in task_dict:
        #         task_dict[x] = -1
        #     elif task_dict[x] == -1:
        #         task_dict[x] = 2
        #     elif task_dict[x] == 2:
        #         rounds += 1
        #         task_dict[x] = 0
        #     else: 
        #         task_dict[x] += 1

        
        # for x in task_dict.values():
        #     if x == -1:
        #         return -1
        #     elif x > 0:
        #         rounds += 1
                
        # return rounds