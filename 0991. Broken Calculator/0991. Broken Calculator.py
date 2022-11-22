class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        if startValue > target:
            return startValue - target
        ops = 0
        while target != startValue:
            if target % 2:
                target += 1
                ops += 1
            if target > startValue:  # and target // 2 > startValue:
                target = target // 2
                ops += 1
            if target < startValue:
                ops += startValue - target
                break
        return ops


test = Solution()
print(test.brokenCalc(3, 647))
