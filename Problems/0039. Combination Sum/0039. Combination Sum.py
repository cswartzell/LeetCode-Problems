class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        counts = collections.Counter(candidates)
        order = sorted(counts.keys())

        ans = []

        # def backtrack(curr_sum, order_idx, curr_run)
        #     if curr_sum > target or order_idx == len(order):
        #         return
        #     if curr_sum == target:
        #         ans.append(curr_run)
        #         return

        #     backtrack(curr_sum, order_idx + 1, curr_run)

        #     order_cnt = counts[order[order_idx]]
        #     curr_run += [order[order_idx] for _ in range(order_cnt)


