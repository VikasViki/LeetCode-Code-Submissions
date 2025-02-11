class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero_index = 0
        zero_index = 0
        nums_len = len(nums)

        while zero_index < nums_len:

            if nums[zero_index] != 0:
                nums[non_zero_index], nums[zero_index] = nums[zero_index], nums[non_zero_index]
                non_zero_index += 1

            zero_index += 1