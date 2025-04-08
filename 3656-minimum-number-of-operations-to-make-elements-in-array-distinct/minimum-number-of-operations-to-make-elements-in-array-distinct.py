class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        seen = set()
        nums_len = len(nums)
        for index in range(nums_len-1, -1 , -1):
            num = nums[index]
            if num in seen:
                return index // 3 + 1
            seen.add(num)
        
        return 0