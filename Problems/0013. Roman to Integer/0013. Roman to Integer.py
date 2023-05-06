#hmmm... cant simply make them constants. Can use a dict I guess?

class Solution:
    def romanToInt(self, s: str) -> int:
#         rom_to_int = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
#         sum = rom_to_int[s[-1]]
        
#         for i in range(len(s)-1):
#             if rom_to_int[s[i+1]] > rom_to_int[s[i]]:
#                 sum -= rom_to_int[s[i]]
#             else:
#                 sum += rom_to_int[s[i]]
#         return sum 