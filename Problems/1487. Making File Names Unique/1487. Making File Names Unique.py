# 04-04-2023 Leetcode 1487. Making File Names Unique
# https://leetcode.com/problems/making-file-names-unique/description/


class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        # names_used = {}
        # ans = []
        # for name in names:
        #     if name in names_used:
        #         while name + F"({names_used[name]})" in names_used:
        #             names_used[name] += 1
        #         name += F"({names_used[name]})"
        #     ans.append(name)
        #     names_used[name] = 1

        # return ans
        # names_used = set

        if not names or names == []:
            return []

        ans = collections.defaultdict(int)
        for name in names:
            if name in ans:
                k = 1
                while name + f"({k})" in ans:
                    k += 1
                name += f"({k})"
            ans[name] = 0
        return ans.keys()
