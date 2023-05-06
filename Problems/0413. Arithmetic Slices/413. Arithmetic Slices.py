class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        head_consec = []
        num_arithm_subsets = 0

        for i in range(len(nums) - 2):
            if nums[i + 1] - nums[i] == nums[i + 2] - nums[i + 1]:
                head_consec.append(i)
        # if nums[-2]-nums[-3] == nums[-1]-nums[-2]:
        #     head_consec.append(len(nums)-2)
        #     head_consec.append(len(nums)-1)
        # print(head_consec)

        for k in range(2, len(nums) - 1):
            for x in head_consec:
                if x + k < len(nums):
                    num_arithm_subsets += 1
