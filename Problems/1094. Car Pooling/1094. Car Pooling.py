# 04-11-2023 Leetcode 1094. Car Pooling
# https://leetcode.com/problems/car-pooling/description/

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # last_stop = max(to for _, _, to in trips)
        # people_in_car_at = [0]*last_stop

        # for num_passengers, fro, to in trips:
        #     for i in range(fro, to):
        #         people_in_car_at[i] += num_passengers
        #         if people_in_car_at[i] > capacity:
        #             return False
        # return True

        # people_in_car_at = []
        # for num_passengers, fro, to in trips:
        #     if len(people_in_car_at) < to:
        #       people_in_car_at += [0 for _ in range(to - len(people_in_car_at))]  
        #     for i in range(fro, to):
        #         people_in_car_at[i] += num_passengers
        #         if people_in_car_at[i] > capacity:
        #             return False
        # return True

        # change = [(at, getting_on) for getting_on, at, _ in trips] + [(at, -getting_off) for getting_off, _, at in trips] 
        # change.sort()
        # for stop, new_change in change:
        #     capacity -= new_change
        #     if capacity < 0:
        #         return False
        # return True


        timestamp = [0]
        for trip in trips:
            if len(timestamp) <= trip[2]:
                timestamp += [0] * (trip[2] - len(timestamp) + 1) 
            timestamp[trip[1]] += trip[0]
            timestamp[trip[2]] -= trip[0]

        used_capacity = 0
        for passenger_change in timestamp:
            used_capacity += passenger_change
            if used_capacity > capacity:
                return False

        return True

        # timestamp = [0]*1001
        # for trip in trips: 
        #     timestamp[trip[1]] += trip[0]
        #     timestamp[trip[2]] -= trip[0]

        # used_capacity = 0
        # for passenger_change in timestamp:
        #     used_capacity += passenger_change
        #     if used_capacity > capacity:
        #         return False

        # return True