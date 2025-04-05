class Solution:

    def calculate_subset_xor_sum(self, index, subset_xor):
        if index == self.nums_len:
            self.xor_sum += subset_xor
            return
        
        # Include
        self.calculate_subset_xor_sum(index+1, subset_xor ^ self.nums[index])

        # Exclude
        self.calculate_subset_xor_sum(index+1, subset_xor)

    def subsetXORSum(self, nums: List[int]) -> int:
        self.xor_sum = 0
        self.nums = nums
        self.nums_len = len(nums)
        self.calculate_subset_xor_sum(0, 0)
        return self.xor_sum