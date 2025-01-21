class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        first_row_suffix = sum(grid[0])
        second_row_prefix = 0
        total_cols = len(grid[0])
        robot_2_points = float('inf')

        for turn_index in range(total_cols):
            first_row_suffix -= grid[0][turn_index]
            robot_2_points = min(robot_2_points, max(first_row_suffix,second_row_prefix) )
            second_row_prefix += grid[1][turn_index]
        
        return robot_2_points
