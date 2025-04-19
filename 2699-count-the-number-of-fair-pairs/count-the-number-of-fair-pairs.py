class Solution:

    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        fair_pairs = 0
        nums_len = len(nums)
        for i, num in enumerate(nums):
            lower_target = lower - num
            left_index = bisect_left(nums, lower_target, lo=i+1)
            upper_target = upper - num + 1
            right_index = bisect_left(nums, upper_target, lo=i+1)
            fair_pairs += right_index - left_index
        
        return fair_pairs