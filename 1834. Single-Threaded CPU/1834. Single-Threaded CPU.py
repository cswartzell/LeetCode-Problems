# 12-29-2022 Leetcode 1834. Single-Threaded CPU
# https://leetcode.com/problems/single-threaded-cpu/description/

# Push tasks into a minHeap as they become available to process?
# This is a priority queue question.

# sort first by enqueTime, then by processing time. sorted() does This
# for tuples intrinsicly. Seperately, keep a minHeap for AVAILABLE tasks.
# As we tick "clock time" add to minheap a new tule: (processtime, INDEX)
# Note, we no longer care about enqueue time.

# Wait, how do I know when the last start time is? Am I going to have to do
# a pass just to search for that?

# Wow. I really liked this one. AND my solution is practically IDENTICAL
# to the given one, without missing any special tricks


class Solution:
    def getOrder(self, taskz: List[List[int]]) -> List[int]:
        # include the index as a third element of tuple
        # sort them, FIRST by enqueTime, then processtime, then by index
        tasks = sorted([[x[0], x[1], y] for y, x in enumerate(taskz)], reverse=True)
        # start clock to first enqueing time. If this was a real simulation we'd just
        # start at zero and advance the clock by 1. Not sure if I should optimize this
        # as a "find out the order asap, not simulate" or leave it as a simulation?
        clock = tasks[-1][0]
        available = []
        processed = []

        while tasks or available:
            while tasks and tasks[-1][0] <= clock:
                next_task = tasks.pop()
                heapq.heappush(available, [next_task[1], next_task[2]])
            if not available and tasks:
                next_task = tasks.pop()
                clock = next_task[0]
                heapq.heappush(available, [next_task[1], next_task[2]])

            curr_task = heapq.heappop(available)
            clock += curr_task[0]
            processed.append(curr_task[1])

        return processed

        # task_dict = collections.defaultdict(list)
        # for idx, enq_pt in enumerate(tasks):
        #     task_dict[enq_pt[0]] += [enq_pt[1], idx]

        # clock = min(task_dict.keys())
        # task_heap = []
        # task_order = []
        # while task_dict:
        #     for key in task_dict.keys():
        #         if key <= clock:
        #             for x in task_dict[key]:
        #                 heapq.heappush(task_heap, x)
        #             del task_dict[x]
        #         else:
        #             break
        #     next_task = heapq.heappop(task_heap)
        #     task_order += next_task[1]
        #     clock += next_task[0]

        # return task_order
