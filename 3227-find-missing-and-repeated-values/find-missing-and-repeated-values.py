class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        matrix_sum = 0
        n = len(grid)
        values_set = set()
        duplicate = None

        for row in grid:
            for value in row:
                if value in values_set:
                    duplicate = value
                values_set.add(value)
                matrix_sum += value
        
        n_square = n*n
        missing = ((n_square * (n_square+1))//2) - (matrix_sum-duplicate)

        return [duplicate, missing]
        

