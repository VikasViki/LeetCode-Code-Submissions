class Solution:

    directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

    def get_fish_catched(self, start_row, start_col):
        queue = deque([(start_row, start_col, self.grid[start_row][start_col])])
        self.visited.add((start_row, start_col))
        total_fish_catched = 0

        while queue:
            row, col, fish_catched = queue.popleft()
            total_fish_catched += fish_catched
            for direction_x, direction_y in self.directions:
                new_row = row + direction_x
                new_col = col + direction_y
                if (new_row, new_col) in self.visited: continue
                if 0 <= new_row < self.total_rows \
                and 0 <= new_col < self.total_cols \
                and self.grid[new_row][new_col] > 0:
                    queue.append((new_row, new_col, self.grid[new_row][new_col]))
                    self.visited.add((new_row, new_col))

        return total_fish_catched


    def findMaxFish(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.total_rows = len(self.grid)
        self.total_cols = len(self.grid[0])
        max_fish_catched = 0
        self.visited = set()
        for row in range(self.total_rows):
            for col in range(self.total_cols):
                if self.grid[row][col] > 0 and (row, col) not in self.visited:
                    fish_catched = self.get_fish_catched(row, col)
                    max_fish_catched = max(max_fish_catched, fish_catched)
        return max_fish_catched