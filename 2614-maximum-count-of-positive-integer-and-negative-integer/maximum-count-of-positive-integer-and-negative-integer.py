class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        last_negative = bisect_left(nums, 0)
        first_positive = bisect_right(nums, 0)
        nums_len = len(nums)
        return max(last_negative, nums_len-first_positive)
        
