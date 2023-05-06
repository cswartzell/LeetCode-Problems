def twoSum():
    nums = [2, 7, 11, 15]
    target = 9

    # for i in range(len(nums)):
    #     for j in range(i+1, len(nums)):
    #         if nums[i] + nums[j] == target:
    #             return [i, j]

    # dictio = {}
    # for i in range(len(nums)):
    #     if str(target - nums[i]) in dictio:
    #         return [i, dictio[str(target - nums[i])]]
    #     dictio.update({str(nums[i]): i})

    dictio = {}
    for i in range(len(nums)):
        if target - nums[i] in dictio:
            return [i, dictio.get(target - nums[i])]
        dictio.update({nums[i]: i})


print(twoSum())
