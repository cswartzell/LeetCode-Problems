# 1477. Find Two Non-overlapping Sub-arrays Each With Target Sum

# Rather, oh good: Positive only. (00700) has 9 subarrays that 
# sum to 7. Only one of len 1 though, so its possible a naive
# solution that ignores subarrays with leading or trailing zeros
# might be fine, since we are explicitly looking for shortest

class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int: 
        R, L, curr_sum = 0,0,0
        subs = []
        while R < len(arr) or curr_sum >= target:
            if curr_sum < target and R < len(arr):
                curr_sum += arr[R]
                R += 1
            else:
                if curr_sum == target:
                    subs.append((R-L, L, R-1))
                curr_sum -= arr[L]
                L += 1
        

        LEN, START, END = 0, 1, 2
        subs.sort()
        min_sum = len(arr) + 1
        i, j = 0, 0
        for i in range(len(subs) - 1):
            if subs[i][LEN] == min_sum - 1:
                break 
            for j in range(i+1, len(subs)):
                if subs[j][LEN] == min_sum - i:
                    break 
                if subs[i][END] < subs[j][START] or subs[i][START] > subs[j][END]:
                    min_sum = min(min_sum, subs[i][LEN] + subs[j][LEN])
        return min_sum if min_sum < len(arr) + 1 else -1

