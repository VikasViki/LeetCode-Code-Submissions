class Solution:

    def calculate_subset_xor_sum(self, index, subset_xor):

        key = (index, subset_xor)
        if key in self.memo:
            return self.memo[key]

        if index == self.nums_len:
            return subset_xor
        
        # Include
        include_val = self.calculate_subset_xor_sum(index+1, subset_xor ^ self.nums[index])

        # Exclude
        exclude_val = self.calculate_subset_xor_sum(index+1, subset_xor)

        self.memo[key] = include_val + exclude_val

        return self.memo[key]

    def subsetXORSum(self, nums: List[int]) -> int:
        self.nums = nums
        self.nums_len = len(nums)
        self.memo = {}
        return self.calculate_subset_xor_sum(0, 0)