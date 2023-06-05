# 05-04-2023 Leetcode 1232. Check If It Is a Straight Line
# https://leetcode.com/problems/check-if-it-is-a-straight-line/description/

# Points are on the same line if: 
# A) Their slopes are the same: rise/run
# B) They have the same Y intercept: y = mx + b so y - slope x = b

# So pick any two points as a our basis, may as well
# be first two. Set yint and slope and just check the rest
# of the points against the starting point. 

# VERY slight optomization: check two new points against eachother
# until there are an odd number of points. 

#Check for div by zero!

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        # if len(coordinates) == 2:
        #     return True

        # #Horizontal Line
        # if coordinates[0][1] == coordinates[1][1]:
        #     for point in coordinates[2:]:
        #         if point[1] != coordinates[0][1]:
        #             return False
        #     return True 
        
        #Vertical Line
        if coordinates[0][0] == coordinates[1][0]:
            for point in coordinates[2:]:
                if point[0] != coordinates[0][0]:
                    return False
            return True

        # Any other line
        slope = (coordinates[0][1] - coordinates[1][1]) / (coordinates[0][0] - coordinates[1][0])
        yint = coordinates[0][1] - coordinates[0][0] * slope

        # Any other line
        slope = (coordinates[0][1] - coordinates[1][1]) / (coordinates[0][0] - coordinates[1][0])
        yint = coordinates[0][1] - coordinates[0][0] * slope

        for i in range(2, len(coordinates)):
            #vertical line, already covered. Exit
            if coordinates[i][0] == coordinates[0][0] \
            or (coordinates[i][1] - coordinates[0][1]) / (coordinates[i][0] - coordinates[0][0]) != slope \
            or coordinates[i][1] - coordinates[i][0] * slope != yint:
                return False
        return True
            





        # if len(coordinates) & 1:
        #     coordinates += [coordinates[0]]
        # for i in range(len(coordinates[2:])):
        #     if coordinates[i][0] == coordinates[i+1][0] \
        #     or (coordinates[i][1] - coordinates[i+1][1]) / (coordinates[i][0] - coordinates[i+1][0]) != slope \
        #     or coordinates[i][1] - coordinates[i][0] * slope != yint \
        #     or coordinates[i+1][1] - coordinates[i+1][0] * slope != yint:
        #         return False
        # return True
            

