# 07-14-2023 Leetcode 207. Course Schedule
# https://leetcode.com/problems/course-schedule/description/

# I think I can use Khans algo?

from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        needs_req = defaultdict(set)
        req_for = defaultdict(set)

        # Adjacency dict for graph for both directions
        for course, pre_req in prerequisites:
            needs_req[course].add(pre_req)
            req_for[pre_req].add(course)

        # Start a stack with all courses that dont have prerequisites
        stack = [course for course in range(numCourses) if course not in needs_req] # Default key causes error?
        
        while stack:
            curr_course = stack.pop()
            for future_course in req_for[curr_course]:
                needs_req[future_course].remove(curr_course)
                if len(needs_req[future_course]) == 0:
                    stack.append(future_course)
                    del needs_req[future_course]
        
        return len(needs_req) == 0