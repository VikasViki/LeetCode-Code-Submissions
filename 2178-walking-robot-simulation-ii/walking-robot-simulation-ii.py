class Robot:

    def __init__(self, width: int, height: int):
        self.moved = False
        self.index = 0
        self.positions = list()
        self.directions = list()

        for index in range(width):
            self.positions.append((index, 0))
            self.directions.append("East")
        
        for index in range(1, height):
            self.positions.append((width-1, index))
            self.directions.append("North")
        
        for index in range(width-2, -1, -1):
            self.positions.append((index, height-1))
            self.directions.append("West")
        
        for index in range(height-2, 0, -1):
            self.positions.append((0, index))
            self.directions.append("South")
        
        self.directions[0] = "South"

        self.total_positions = len(self.positions)

        

    def step(self, num: int) -> None:
        self.moved = True
        self.index = ( self.index + num ) % self.total_positions
        

    def getPos(self) -> List[int]:
        return list(self.positions[self.index])
        

    def getDir(self) -> str:
        if not self.moved:
            return "East"
        return self.directions[self.index]
        


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()