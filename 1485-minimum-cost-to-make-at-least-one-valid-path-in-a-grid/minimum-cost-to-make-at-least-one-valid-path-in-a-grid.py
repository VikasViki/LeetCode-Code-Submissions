class Solution:

    _directions = {
        1: (0, 1),
        2: (0, -1),
        3: (1, 0),
        4: (-1, 0)
    }

    def minCost(self, grid: List[List[int]]) -> int:
        total_rows, total_cols = len(grid), len(grid[0])
        queue = deque([(0, 0, 0)])
        min_cost = { (0,0): 0 }

        while queue:
            row, col, cost = queue.popleft()
            
            for d in self._directions:
                d_row, d_col = self._directions[d]
                new_row, new_col = row + d_row, col + d_col
                new_cost = cost if grid[row][col] == d else cost+1

                if (
                    new_row < 0 or new_col < 0 or \
                    new_row == total_rows or new_col == total_cols or \
                    new_cost >= min_cost.get((new_row, new_col), float('inf'))
                ):
                    continue
                
                min_cost[(new_row, new_col)] = new_cost

                if grid[new_row][new_col] == d:
                    queue.appendleft((new_row, new_col, new_cost))
                else:
                    queue.append((new_row, new_col, new_cost))
        
        return min_cost[(total_rows-1, total_cols-1)]
