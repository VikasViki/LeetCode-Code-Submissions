class Solution:

    def __init__(self):
        # (cur__direction, command)
        self.next_direction = {
            ("N", -1) : ("E", 1, 0),
            ("N", -2) : ("W", -1, 0),
            ("E", -1) : ("S", 0, -1),
            ("E", -2) : ("N", 0, 1),
            ("S", -1) : ("W", -1, 0),
            ("S", -2) : ("E", 1, 0),
            ("W", -1) : ("N", 0, 1),
            ("W", -2) : ("S", 0, -1)
        }

    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        self.curr_direction = "N"
        self.dx = 0
        self.dy = 1
        obstacles = set(map(tuple, obstacles))
        robot_x = 0
        robot_y = 0

        max_euclidean_distance = float('-inf')

        for command in commands:
            if command > 0:
                for step in range(1, command+1):
                    robot_x += self.dx
                    robot_y += self.dy
                    if (robot_x, robot_y) in obstacles:
                        robot_x -= self.dx
                        robot_y -= self.dy
                        break
            else:
                self.curr_direction, self.dx, self.dy = self.next_direction.get((self.curr_direction, command))
            
            euclidean_distance = robot_x**2 + robot_y**2
            max_euclidean_distance = max(max_euclidean_distance, euclidean_distance)
        
        return max_euclidean_distance