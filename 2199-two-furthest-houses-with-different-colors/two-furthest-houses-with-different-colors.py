class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        total_colors = len(colors)
        max_distance = 0
        for start in range(total_colors):
            for end in range(total_colors-1, -1, -1):
                if colors[start] != colors[end]:
                    distance = abs(start-end)
                    break
            max_distance = max(max_distance, distance)
        
        return max_distance
