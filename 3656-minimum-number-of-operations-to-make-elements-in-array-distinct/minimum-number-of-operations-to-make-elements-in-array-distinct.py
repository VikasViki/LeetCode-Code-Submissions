class Solution:

    def is_unique(self, freq):
        for num, count in freq.items():
            if count > 1:
                return False
        return True

    def minimumOperations(self, nums: List[int]) -> int:
        freq = Counter(nums)
        operations = 0
        if self.is_unique(freq):
            return operations
        
        nums_len = len(nums)
        if nums_len <= 3:
            return 1
        
        for index in range(0, nums_len-3, 3):
            num1, num2, num3 = nums[index: index+3]
            freq[num1] -= 1
            freq[num2] -= 1
            freq[num3] -= 1
            operations += 1
            if self.is_unique(freq):
                return operations
        
        return operations + 1
