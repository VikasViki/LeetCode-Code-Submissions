PASCAL = [[1], [1,1]]

for row in range(2, 31):
    curr_row = [1]
    for index in range(1, row):
        curr_row += [PASCAL[row-1][index]+PASCAL[row-1][index-1]]
    curr_row += [1]
    PASCAL += [curr_row[::]]

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        return PASCAL[:numRows]