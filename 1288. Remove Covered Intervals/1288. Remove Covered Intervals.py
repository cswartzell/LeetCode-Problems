""" 02-19-2022 Leetcode 1288. Remove Covered Intervals """
intervals = [[1, 4], [3, 6], [2, 8]]
intervalas_copy = intervals.copy()
i = 0
j = 0

for curr_interval in intervalas_copy:
    while j < len(intervals):
        dele_interval = intervals[j]
        if (
            curr_interval[0] <= intervals[j][0]
            and curr_interval[1] >= intervals[j][1]
            and curr_interval != dele_interval
        ):
            del intervals[j]
            j -= 1
        j += 1
    j = 0
print(len(intervals))
