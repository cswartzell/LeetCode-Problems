class Solution:
    def findPaths(
        self, m: int, n: int, maxMove: int, startRow: int, startColumn: int
    ) -> int:
        oob_count = 0
        n, m = n - 1, m - 1
        mod_it = 10 ** 9 + 7

        @cache
        def pass_it(i, j, kicks, oob_count):
            if kicks == maxMove or i < 0 or i > m or j < 0 or j > n:
                return 0
            return (
                pass_it(i + 1, j, kicks + 1, oob_count) % mod_it
                + pass_it(i, j + 1, kicks + 1, oob_count) % mod_it
                + pass_it(i - 1, j, kicks + 1, oob_count) % mod_it
                + pass_it(i, j - 1, kicks + 1, oob_count) % mod_it
                + (i == 0)
                + (i == m)
                + (j == 0)
                + (j == n)
            )

        return pass_it(startRow, startColumn, 0, 0) % mod_it
