class Solution:

    def is_out_of_bound(self, row, col):
        return (not (0 <= row < self.total_rows)) or (not (0 <= col < self.total_cols))

    def get_max_cherries(self, r1_row, r1_col, r2_row, r2_col):
        if self.is_out_of_bound(r1_row, r1_col):
            return 0
        if self.is_out_of_bound(r2_row, r2_col):
            return 0
        
        key = (r1_row, r1_col, r2_row, r2_col)

        if key in self.memo:
            return self.memo[key]
        
        max_score = 0

        for new_r1_col in [r1_col-1, r1_col, r1_col+1]:
            for new_r2_col in [r2_col-1, r2_col, r2_col+1]:
                r1_cell = self.grid[r1_row][r1_col]
                r2_cell = self.grid[r2_row][r2_col] if (r1_row, r1_col) != (r2_row, r2_col) else 0
                curr_score = r1_cell + r2_cell + \
                self.get_max_cherries(r1_row+1, new_r1_col, r2_row+1, new_r2_col)
                max_score = max(curr_score, max_score)
        
        self.memo[key] = max_score
        
        return max_score

    def cherryPickup(self, grid: List[List[int]]) -> int:
        self.memo = {}
        self.grid = grid
        self.total_rows = len(self.grid)
        self.total_cols = len(self.grid[0])
        max_score = self.get_max_cherries(0, 0, 0, self.total_cols-1)
        return max_score