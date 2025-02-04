class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_ascending_sum = nums[0]
        ascending_sum = nums[0]
        nums_len = len(nums)
        for index in range(1, nums_len):
            if nums[index] > nums[index-1]:
                ascending_sum += nums[index]
            else:
                ascending_sum = nums[index]
            max_ascending_sum = max(max_ascending_sum, ascending_sum)
        return max_ascending_sum

