class Solution:

    def flatten_factory(self, factory):
        factory_positions = []
        for position, limit in factory:
            factory_positions += [position] * limit
        return factory_positions
    
    def calculate_minimum_distance(self, robot_index, factory_index):

        if (robot_index, factory_index) in self.memo:
            return self.memo[(robot_index, factory_index)]

        # Base case
        if robot_index == len(self.robot_positions):
            return 0
        if factory_index == len(self.factory_positions):
            return float('inf')
        
        distance = abs(self.robot_positions[robot_index] - self.factory_positions[factory_index])
        
        assign = distance + self.calculate_minimum_distance(robot_index+1, factory_index+1)
        skip = self.calculate_minimum_distance(robot_index, factory_index+1)

        self.memo[(robot_index, factory_index)] = min(assign, skip)

        return self.memo[(robot_index, factory_index)]


    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort(key=lambda x:x[0])
        factory_positions = self.flatten_factory(factory)
        self.robot_positions = robot
        self.factory_positions = factory_positions
        self.memo = {}
        min_distance = self.calculate_minimum_distance(0, 0)
        return min_distance
