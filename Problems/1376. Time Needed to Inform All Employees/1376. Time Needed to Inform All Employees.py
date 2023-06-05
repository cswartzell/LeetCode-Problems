# 05-04-2023 Leetcode 1376. Time Needed to Inform All Employees
# https://leetcode.com/problems/time-needed-to-inform-all-employees/description/

# Make a manages dict, where id is the key, and th list is employees. Keep a visited list
# We cont just check the slowest on each leg as mabe a bunch of legs will be fast, then suddenly
# there is an interminable time. We will need to DFS the whoe tree and each leaf note if this route
# took more time than previous

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        # manages = collections.defaultdict(list)
        # for employee in range(len(manager)):
        #     manages[manager[employee]].append(employee)

        # self.maxTime = 0
        # def DFS(manager, timeSoFar):
        #     if manager not in manages:
        #         self.maxTime = max(self.maxTime, timeSoFar)
        #     for subordinate in manages[manager]:
        #         DFS(subordinate, timeSoFar + informTime[manager])
        
        # DFS(headID, 0)
        # return self.maxTime

        @cache
        def get_notification_time(i):
            if (manager_id := manager[i]) != -1:
                return informTime[manager_id] + get_notification_time(manager_id)
            else:
                return 0

        return max(get_notification_time(i) for i in range(n))