class Solution:
    def check(self, nums: List[int]) -> bool:
        nums_len = len(nums)
        if nums_len <= 1:
            return True
        
        inversion_count = 0
        for index in range(1, nums_len):
            if nums[index] < nums[index-1]:
                inversion_count += 1
        
        # check border elements
        if nums[0] < nums[-1]:
            inversion_count += 1
        
        return inversion_count <= 1