class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        total_nums = len(nums)
        nums_sum = 0
        f = 0
        for index, num in enumerate(nums):
            nums_sum += num
            f += index * num

        max_f = f
        last_index = -1
        for k in range(total_nums):
            new_f = f + nums_sum - total_nums * nums[last_index]
            last_index -= 1
            f = new_f
            max_f = max(max_f, f)
        
        return max_f
