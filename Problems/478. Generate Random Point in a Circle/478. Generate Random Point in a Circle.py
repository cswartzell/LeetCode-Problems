#python.exe -m pip install --upgrade pip
#python3 -m venv MY_ENV       (If it fails on windows, try removing the "3")
#venv/Scripts/activate    IF ON WINDOWS
#source MY_ENV/bin/activate  MacOS/UNIX
#pip install matplotlib



import matplotlib.pyplot as plt
import random
import math
from typing import List


class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.x_min, self.x_max = x_center - radius, x_center + radius
        self.y_min, self.y_max = y_center - radius, y_center + radius
        self.h, self.k = x_center,  y_center
        self.r, self.rsq = radius, radius**2

    def randPoint(self) -> List[float]:
        x = random.uniform(self.x_min, self.x_max)
        y_range = math.sqrt(self.rsq -(x-self.h)**2)
        y = random.uniform(self.k - y_range, self.k + y_range)
        
        # print("stdout works")
        check_x_min = self.h - self.r <= x 
        check_x_max = x <= self.h + self.r
        check_y_min = self.k - self.r <= y 
        check_y_max = y <= self.k + self.r
        check_d = (d := (x-self.h)**2 + (y-self.k)**2 < self.rsq)
        if not (check_x_min and check_x_max and check_y_min and check_y_max and check_d):     
            print(f"X: {x}, Y: {y}, D: {d} FAILS!!!! ")
            if not check_x_min:
                print(f"xmin: {self.h - self.r}")
            if not check_x_max:
                print(f"xmax: {self.h + self.r}")
            if not check_y_min:
                print(f"ymin: {self.k - self.r}")
            if not check_y_max:
                print(f"ymax: {self.k + self.r}")
            if not check_d:
                print(f"D: {d} dmax: {self.rsq}")

        return [x,y]

test = Solution(1, 1.5, 1.5)

plt.axis([0, 3, 0, 3])
plt.axis('square')

for i in range(100):
    x, y = [], []
    for j in range(100):
        point = test.randPoint()
        x.append(point[0])
        y.append(point[1]) 
    plt.scatter(x,y)
    plt.draw() 
    plt.pause(0.1)

