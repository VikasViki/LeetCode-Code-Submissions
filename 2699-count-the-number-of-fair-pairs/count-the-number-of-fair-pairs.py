class Solution:

    def lower_bound_binary_search(self, nums, low, high, target):
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] >= target:
                high = mid - 1
            else:
                low = mid + 1
        return low

    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        fair_pairs = 0
        nums_len = len(nums)
        for index, num in enumerate(nums):
            lower_target = lower - num
            left_index = self.lower_bound_binary_search(nums, index+1, nums_len-1, lower_target)
            upper_target = upper - num + 1
            right_index = self.lower_bound_binary_search(nums, index+1, nums_len-1, upper_target)
            fair_pairs += right_index - left_index
        
        return fair_pairs