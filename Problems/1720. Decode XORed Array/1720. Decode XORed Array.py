# 03-24-2024 Leetcode 1720. Decode XORed Array
# https://leetcode.com/problems/decode-xored-array/
# time: 2 mins, challenge 2/10
class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        arr = [first]
        for num in encoded:
            arr.append(num^arr[-1])
        return arr
