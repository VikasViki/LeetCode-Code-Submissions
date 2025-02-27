class Solution:

    def generate_all_permutations(self, nums, start_index):
        if start_index == len(nums):
            self.permutations.append(nums[:])
            return
        
        for index in range(start_index, len(nums)):
            nums[start_index], nums[index] = nums[index], nums[start_index]
            self.generate_all_permutations(nums, start_index+1)
            nums[start_index], nums[index] = nums[index], nums[start_index]


    def permute(self, nums: List[int]) -> List[List[int]]:
        self.permutations = []
        self.generate_all_permutations(nums, 0)
        return self.permutations