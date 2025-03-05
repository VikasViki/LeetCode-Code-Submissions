class Solution:
    def coloredCells(self, n: int) -> int:
        total_blue_cells = 0
        curr_row = (2*n)-1
        while curr_row >= 1:
            total_blue_cells += (curr_row * 2)
            curr_row -= 2
        return total_blue_cells - ((2*n)-1)
     


