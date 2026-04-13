class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        min_distance = float('inf')
        for index, num in enumerate(nums):
            if num == target:
                curr_distance = abs(index-start)
                min_distance = min(min_distance, curr_distance)
        return min_distance