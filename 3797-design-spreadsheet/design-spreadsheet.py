class Spreadsheet:

    def __init__(self, rows: int):
        self.sheet = [ [0] * 26 for row in range((10**3)+1)]
        self.char_to_col = {char:index for index, char in enumerate(ascii_uppercase)}
    
    def get_row_and_col(self, cell: str) -> Tuple[int, int]:
        char, row = cell[0], int(cell[1:])
        col = self.char_to_col[char]
        return (row, col)

    def setCell(self, cell: str, value: int) -> None:
        row, col = self.get_row_and_col(cell)
        self.sheet[row-1][col] = value

    def resetCell(self, cell: str) -> None:
        row, col = self.get_row_and_col(cell)
        self.sheet[row-1][col] = 0
    
    def get_value_from_sheet(self, val: str) -> int:
        if val.isdigit():
            return int(val)
        row, col = self.get_row_and_col(val)
        return self.sheet[row-1][col]
        
    def getValue(self, formula: str) -> int:
        val1, val2 = formula[1:].split("+")
        sheet_val1 = self.get_value_from_sheet(val1)
        sheet_val2 = self.get_value_from_sheet(val2)
        return sheet_val1 + sheet_val2
        


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)