class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
        total_rows = len(heightMap)
        total_cols = len(heightMap[0])

        visited = set()
        min_heap = []

        for row in range(total_rows):
            for col in range(total_cols):
                if row in {0, total_rows-1} or col in {0, total_cols-1}:
                    cell_height = heightMap[row][col]
                    heappush(min_heap, (cell_height, row, col))
                    visited.add((row, col))
        
        water_trapped = 0

        while min_heap:
            cell_height, row, col = heappop(min_heap)

            for dir_row, dir_col in directions:
                neighbor_row = row + dir_row
                neighbor_col = col + dir_col
                if 0 <= neighbor_row < total_rows and 0 <= neighbor_col < total_cols and\
                (neighbor_row, neighbor_col) not in visited:
                
                    neighbor_height = heightMap[neighbor_row][neighbor_col]
                    if neighbor_height < cell_height:
                        water_trapped += cell_height - neighbor_height

                    heappush(min_heap, (max(neighbor_height, cell_height), neighbor_row, neighbor_col))

                    visited.add((neighbor_row, neighbor_col))
        
        return water_trapped
