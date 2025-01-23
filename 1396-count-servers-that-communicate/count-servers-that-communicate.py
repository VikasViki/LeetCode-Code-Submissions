class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        servers_in_row = {}
        servers_in_col = {}
        total_rows = len(grid)
        total_cols = len(grid[0])

        for row in range(total_rows):
            for col in range(total_cols):
                if grid[row][col] == 1:
                    servers_in_row[row] = servers_in_row.get(row, 0) + 1
                    servers_in_col[col] = servers_in_col.get(col, 0) + 1
        
        communicating_servers = 0
        for row in range(total_rows):
            for col in range(total_cols):
                if grid[row][col] == 1:
                    if servers_in_row[row] > 1 or servers_in_col[col] > 1:
                        communicating_servers += 1
        
        return communicating_servers