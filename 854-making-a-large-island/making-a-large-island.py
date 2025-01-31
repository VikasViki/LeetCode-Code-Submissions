class Solution:
    def __init__(self):
        self.directions = ((0, -1), (0, 1), (1, 0), (-1, 0))
    
    def get_island_size(self, start_row, start_col, island_num):
        queue = deque([(start_row, start_col)])
        self.visited.add((start_row, start_col))
        island_size = 0
        while queue:
            row, col = queue.popleft()
            self.island_group[row][col] = island_num
            island_size += 1
            for delta_row, delta_col in self.directions:
                new_row = row + delta_row
                new_col = col + delta_col
                if 0 <= new_row < self.total_rows and 0 <= new_col < self.total_cols and\
                (new_row, new_col) not in self.visited and self.grid[new_row][new_col] == 1:
                    queue.append((new_row, new_col))
                    self.visited.add((new_row, new_col))
        return island_size

    def largestIsland(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.total_rows = len(self.grid)
        self.total_cols = len(self.grid[0])
        self.island_group = [ [0] * self.total_cols for row in range(self.total_rows) ]

        self.island_size = {0:0} # All 0's
        self.visited = set()

        water_cells = []
        island_num = 1
        largest_island = 0

        for row in range(self.total_rows):
            for col in range(self.total_cols):
                if (row, col) not in self.visited:
                    if self.grid[row][col] == 1:
                        self.island_size[island_num] = self.get_island_size(row, col, island_num)
                        largest_island = max(largest_island, self.island_size[island_num])
                        island_num += 1
                    else:
                        water_cells.append((row, col))
        
        # print(self.island_size)
        
        for row, col in water_cells:
            neighbor_islands = {}
            for delta_x, delta_y in self.directions:
                new_row = row + delta_x
                new_col = col +  delta_y
                if 0 <= new_row < self.total_rows and 0 <= new_col < self.total_cols:
                    island_num = self.island_group[new_row][new_col]
                    neighbor_islands[island_num] = self.island_size[island_num]
            merged_island = sum(neighbor_islands.values()) + 1
            largest_island = max(largest_island, merged_island)
        
        return largest_island