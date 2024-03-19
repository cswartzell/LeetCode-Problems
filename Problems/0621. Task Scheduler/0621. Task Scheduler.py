# 03-18-2024 Leetcode 621. Task Scheduler
# https://leetcode.com/problems/task-scheduler/?envType=daily-question&envId=2024-03-19
# Time:15 mins Challnege: 3/10 but ive done it before. maybe a solid 4.5/10 otherwise

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        
        TIME_AVAILABLE = 0
        # Tuple: (time_available, reps_remaining, task)
        in_progress = []
        # Tuple: (time_available, reps_remaining, task)
        counts = collections.Counter(tasks)
        # NOTE: as we want the task with the MOST reps remaining, we need a MAXHEAP. 
        available =[(-count, task) for task, count in counts.items()]
        heapq.heapify(available)

        time = 0
        while in_progress or available:
            while in_progress and in_progress[0][TIME_AVAILABLE] < time:
                _,  task = heapq.heappop(in_progress)
                heapq.heappush(available, (-counts[task], task))

            if available:
                _, task = heapq.heappop(available)
                counts[task] -= 1 
                if counts[task]:
                    heapq.heappush(in_progress, (time + n, task))
                time += 1
            else:
                time = in_progress[0][TIME_AVAILABLE] + 1

        return time



# Could use a heap and a clock time. Push all task letters onto the heap 
# with "available at time X" set to 0. Set clock to zero. Start loop:
# If clock time LESS than available time at top of heap, add the difference to
# the count. This is idle ticks. Set clock time to top of heap available CONTINUE
# If clocktime >= top of heap available time, pop top, add the wait time time to
# current clock time and push this letter back into heap with "new available at"
# time. Add 1 to clock.

# Oh, this only solves the scheduling. Now we actually need to do n tasks of each letter.
# Count them, and add them to the there are still copies of said task to do. When we've 
# done the last copy of the task, delete it from to_do counter. DO NOT PUSH BACK TO HEAP

# The obvious issue here is the clock counter is going to run forever. A naive solution might be
# to use a modulo to wrap, but then we'd have small "available" tasks in the heap that are actually
# after big numbers til the clock itself wraps. To solve this we could use TWO heaps and sort of 
# roll back and forth between them... Im going to say too complex for now.


#Aaaaand this fails. Imagaine the tasks ABCDEFGHIJKZZZZZZZ with time of two. Going arbitrarily 
# from the begining we waste no time ripping through a-k with zero idle ticks. Now we get to a
# block of all z, and have to wait a tick between each block. If we had INSTEAD gone 
# zazbzczdzezfzgzhzizjzk we would have powered through all the Zs TOO. So we need to do the 
# MOST needed tasks ahead when there is a tie. SO I think we can modify our heap setup.
# its now a triple (T_AVAILABLE, REMAINING, LETTER) and we can do away with the ditionary.
# We are therefore never waiting unless no tasks available (per above), but when there is a
# tie for avaialability we do the most needed task first, hoping any relative downtime can be filled
# with less common tasks til we are out of tasks. 

# Huh. Weirdly, we dont need the letter actually. We count we need 5 z tasks, and say 3 b tasks, and
# so we push (T_AVAILABLE, REMAINING) for both onto the stack and... never use the letter again.
# We just decrement the remaining in the tuple without regard to the letter. 
#Ugh... remember heapq is minheap only, so negate the number REMAINING and ADD to it. 

# No... this still doesnt work, but I think is very close. Its the follwing:
# Organize by (T_AVAILABLE, REMAINING)... no!!!!


 


# class Solution:
#     def leastInterval(self, tasks: List[str], n: int) -> int:
#         if n == 0:
#             return len(tasks)  
        
#         to_do = collections.Counter(tasks)
#         num_tasks = len(to_do)
#         heap = [-value for value in to_do.values()]
#         heapq.heapify(heap)
#         waiting = collections.deque()
#         for _ in range(n):
#             waiting.append(None)
        
#         cycles = 0

#         while num_tasks > 1:
#             if heap:
#                 curr_task = heapq.heappop(heap)
#                 if curr_task < -1:
#                     waiting.append(curr_task + 1)
#                 else:
#                     num_tasks -= 1
#                     waiting.append(None)
#             else:
#                 waiting.append(None)
            
#             cycles += 1    

#             return_task = waiting.popleft()
#             if return_task:
#                 heapq.heappush(heap, return_task)

#         # Only one task left, but it could be in waiting deque
#         while not heap:
#             cycles += 1
#             return_task = waiting.popleft()
#             if return_task:
#                 heap = [return_task]
        
#         cycles += 1 + -(n+1) * (heap[0] + 1)

#         return cycles


        # if n <= 1:
        #     return len(tasks)
         
        # to_do = collections.Counter(tasks)
        # heap = [(0, to_do[task], task) for task in to_do.keys()]
        # heapq.heapify(heap)
        # clk = 0
        # cycles = 0
        # T_AVAILABLE, REMAINING, LETTER = 0, 1, 2

        # while to_do:
        #     curr_task = heapq.heappop(heap)
        #     if curr_task[T_AVAILABLE] > clk:
        #         cycles += curr_task[T_AVAILABLE] - clk
        #         clk = curr_task[T_AVAILABLE]
        #     clk += 1
        #     cycles += 1
        #     if to_do[curr_task[REMAINING]] != 1:
        #         heapq.heappush(heap, (clk+n, curr_task[REMAINING] -1, curr_task[LETTER]))

        # return cycles

        
        
        
        
        
        
        
        # if n <= 1:
        #     return len(tasks)
        
        # T_AVAILABLE, LETTER = 0, 1 
        # to_do = collections.Counter(tasks)
        # heap = [(0, task) for task in to_do.keys()]
        # clk = 0
        # cycles = 0

        # while to_do:
        #     curr_task = heapq.heappop(heap)
        #     if curr_task[T_AVAILABLE] > clk:
        #         cycles += curr_task[T_AVAILABLE] - clk
        #         clk = curr_task[T_AVAILABLE]
        #     clk += 1
        #     cycles += 1
        #     to_do[curr_task[LETTER]] -= 1
        #     if to_do[curr_task[LETTER]] == 0:
        #         del to_do[curr_task[LETTER]]
        #     else: 
        #         heapq.heappush(heap, (clk+n, curr_task[LETTER]))

        # return cycles
