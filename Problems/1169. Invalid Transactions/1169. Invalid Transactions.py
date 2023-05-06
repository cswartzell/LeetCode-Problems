# 04-27-2023 Leetcode 1169. Invalid Transactions
# https://leetcode.com/problems/invalid-transactions/description/


class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        ans = []
        NameTimeCityAmountAdded = collections.defaultdict(list)
        for transaction in transactions:
            name, time, amount, city = transaction.split(",")
            NameTimeCityAmountAdded[name].append([int(time), city, amount, False])

        time, city, amount, added = 0, 1, 2, 3

        for name in NameTimeCityAmountAdded:
            stack = []
            NameTimeCityAmountAdded[name].sort()
            for tr in NameTimeCityAmountAdded[name]:
                if int(tr[amount]) > 1000:
                    ans.append(",".join([name, str(tr[time]), tr[amount], tr[city]]))
                    tr[added] = True

                i = len(stack) - 1
                stack.append(tr)
                while i >= 0:
                    if int(tr[time]) - int(stack[i][time]) <= 60:
                        if stack[i][city] != tr[city]:
                            if not tr[added]:
                                ans.append(
                                    ",".join(
                                        [name, str(tr[time]), tr[amount], tr[city]]
                                    )
                                )
                                tr[added] = True
                            if not stack[i][added]:
                                ans.append(
                                    ",".join(
                                        [
                                            name,
                                            str(stack[i][time]),
                                            stack[i][amount],
                                            stack[i][city],
                                        ]
                                    )
                                )
                                stack[i][added] = True
                    else:
                        stack = stack[i + 1 :]
                        break
                    i -= 1

        return ans
