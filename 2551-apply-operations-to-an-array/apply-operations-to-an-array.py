class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        # Updating nums
        nums_len = len(nums)
        for index in range(nums_len-1):
            if nums[index] == nums[index+1]:
                nums[index] = nums[index+1] * 2
                nums[index+1] = 0
        
        # moving zeros
        new_nums = [0] * nums_len
        new_nums_index = 0
        for index in range(nums_len):
            if nums[index] != 0:
                new_nums[new_nums_index] = nums[index]
                new_nums_index += 1
        
        return new_nums

