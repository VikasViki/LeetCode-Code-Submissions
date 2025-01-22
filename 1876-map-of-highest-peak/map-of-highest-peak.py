class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
        total_rows = len(isWater)
        total_cols = len(isWater[0])
        
        height_matrix = [ [0] * total_cols for row in range(total_rows)]

        water_nodes = []
        for row in range(total_rows):
            for col in range(total_cols):
                if isWater[row][col] == 1:
                    water_nodes.append((row, col, 0))
        
        queue = deque(water_nodes)

        while queue:
            row, col, height = queue.popleft()

            for dir_x, dir_y in directions:
                new_row = row + dir_x
                new_col = col + dir_y

                if 0 <= new_row < total_rows \
                and 0 <= new_col < total_cols \
                and isWater[new_row][new_col] == 0\
                and height_matrix[new_row][new_col] == 0:

                    height_matrix[new_row][new_col] = height + 1
                    queue.append((new_row, new_col, height+1))
        
        return height_matrix

