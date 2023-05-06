"""2-17-2022 402. Remove K Digits"""


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k == len(num):
            print(0)

        lnum = list(num)
        lnum.append("0")
        start_index = 0

        while lnum and k > 0 and start_index < len(num):
            curr_slice = lnum[start_index : start_index + k + 1]
            if curr_slice[0] > min(curr_slice):
                del lnum[start_index]
                k -= 1
            else:
                start_index += 1
            while lnum and lnum[0] == "0":
                del lnum[0]

        if not lnum:
            return "0"
        else:
            lnum.pop()
            return "".join(lnum)

    num = "10"
    k = 2
    print(removeKdigits(num, k))
