from typing import List
from bisect import bisect_left, bisect_right

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        
        left_index = bisect_left(nums, target)
        right_index = bisect_right(nums, target) - 1

        if left_index >= len(nums) or nums[left_index] != target:
            return [-1, -1]
        
        return [left_index, right_index]
