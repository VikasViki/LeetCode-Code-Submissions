class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero_index = 0
        curr = 0
        nums_len = len(nums)

        while curr < nums_len:

            if nums[curr] != 0:
                nums[non_zero_index], nums[curr] = nums[curr], nums[non_zero_index]
                non_zero_index += 1

            curr += 1