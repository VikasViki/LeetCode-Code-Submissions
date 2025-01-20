class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        total_rows = len(mat)
        total_cols = len(mat[0])

        indices = {}
        row_painted = {row: 0 for row in range(total_rows)}
        col_painted = {col: 0 for col in range(total_cols)}

        for row in range(total_rows):
            for col in range(total_cols):
                value = mat[row][col]
                indices[value] = (row, col)
        
        for index, val in enumerate(arr):
            row, col = indices[val]
            row_painted[row] += 1
            col_painted[col] += 1
            if row_painted[row] == total_cols or col_painted[col] == total_rows:
                return index





