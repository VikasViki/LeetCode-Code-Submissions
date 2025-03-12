class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        nums_len = len(nums)
        left_min = [0] * nums_len

        left_min[0] = nums[0]
        for index in range(1, nums_len):
            left_min[index] = min(left_min[index-1], nums[index])
        
        right_max = [0] * nums_len
        right_max[-1] = nums[-1]
        for index in range(nums_len-2, -1, -1):
            right_max[index] = max(right_max[index+1], nums[index])
        
        
        for index in range(1, nums_len-1):
            num = nums[index]
            if left_min[index-1] < num < right_max[index+1]:
                return True

        return False

