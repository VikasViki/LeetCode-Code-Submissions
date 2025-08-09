class Solution:
    def get_distance(self, point1: List[List[int]], point2: List[List[int]]) -> int:
        x1, y1 = point1
        x2, y2 = point2
        x_val = (x2-x1)**2
        y_val = (y2-y1)**2
        return math.sqrt(x_val+y_val)

    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        total_points = len(points)
        boomerangs = 0

        for i in range(total_points):
            point1 = points[i]
            distance_freq = {}
            for j in range(total_points):
                point2 = points[j]
                points_distance = self.get_distance(point1, point2)
                distance_freq[points_distance] = distance_freq.get(points_distance, 0) + 1
            
            for distance, count in distance_freq.items():
                if count > 1:
                    boomerangs += (count * (count-1))
        
        return boomerangs
            




        