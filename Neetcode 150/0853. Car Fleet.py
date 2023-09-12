# 09-12-2023 Neetcode 853. Car Fleet
# https://leetcode.com/problems/car-fleet/description/
# Time: 40 minutes (mostly refactoring)

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        POS, SPEED = 0, 1
        cars = sorted(zip(position, speed))
        curr_fleet = cars.pop()
        car_fleets = 1

        while cars:
            curr_car = cars.pop()
            
            if curr_car[SPEED] <= curr_fleet[SPEED]:
                distance_meet = target + 1
            else:
                distance_meet = ((curr_fleet[POS] - curr_car[POS]) / (curr_car[SPEED] - curr_fleet[SPEED])) * curr_fleet[SPEED] + curr_fleet[POS]
            
            # Curr_car too slow to catch curr_fleet before target
            if distance_meet > target:
                curr_fleet = curr_car
                car_fleets += 1

        return car_fleets
