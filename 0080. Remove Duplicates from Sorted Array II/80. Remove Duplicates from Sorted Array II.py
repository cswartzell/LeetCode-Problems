nums = [1, 1, 1, 2, 2, 3]

if len(nums) <= 2:
    print(len(nums), nums)
i = 2
while i < len(nums):
    if nums[i] == nums[i - 1] and nums[i] == nums[i - 2]:
        nums.pop(i)
        i -= 1
    i += 1
k = len(nums)
print(k, nums)
