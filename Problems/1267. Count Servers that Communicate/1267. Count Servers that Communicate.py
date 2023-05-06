# 04-09-2023 Leetcode 1267. Count Servers that Communicate
# https://leetcode.com/problems/count-servers-that-communicate/description/

#Union find or BFS. BFS is slightly easier to write

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:            
        def BFS( row_i, col_j ):
            rows_q = [row_i]
            cols_q = [col_j]
            seen_rows = {row_i}
            seen_cols = {col_j}
            count = 0            
            while rows_q or cols_q:
                while rows_q:
                    curr_row = rows_q.pop()
                    for j in range(len(grid[0])):
                        if grid[curr_row][j]:
                            grid[curr_row][j] = 0
                            count += 1
                            if j not in seen_cols:
                                cols_q.append(j)
                                seen_cols.add(j)
                while cols_q:
                    curr_col = cols_q.pop()
                    for i in range(len(grid)):
                        if grid[i][curr_col]:
                            grid[i][curr_col] = 0
                            count += 1
                            if i not in seen_rows:
                                rows_q.append(i)
                                seen_rows.add(i)
            
            return count if count > 1 else 0
        
        ans = 0


        for row_i in range(len(grid)):
            for col_j in range(len(grid[0])):
                if grid[row_i][col_j] == 1:
                    ans += BFS(row_i, col_j)

        return ans