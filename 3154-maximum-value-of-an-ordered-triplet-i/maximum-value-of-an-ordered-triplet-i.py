class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        nums_len = len(nums)
        max_val = 0
        for i in range(nums_len):
            for j in range(i+1, nums_len):
                for k in range(j+1, nums_len):
                    curr_val = (nums[i] - nums[j]) * nums[k]
                    max_val = max(max_val, curr_val)
        return max_val
