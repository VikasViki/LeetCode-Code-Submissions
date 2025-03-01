class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)
        new_nums = [0] * nums_len
        new_num_index = 0

        for index in range(nums_len):
            if index+1 < nums_len and nums[index] == nums[index+1]:
                if nums[index] == 0: continue
                new_nums[new_num_index] = nums[index] * 2
                nums[index+1] = 0
                new_num_index += 1
            else:
                if nums[index] != 0:
                    new_nums[new_num_index] = nums[index]
                    new_num_index += 1

        return new_nums

