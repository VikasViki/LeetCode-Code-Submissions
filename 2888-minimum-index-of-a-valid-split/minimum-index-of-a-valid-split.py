class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        nums_len = len(nums)

        freq = {}
        prefix_dominant = [None] * nums_len
        max_ele = nums[0]
        max_freq = 1
        for index, num in enumerate(nums):
            freq[num] = freq.get(num, 0) + 1
            if freq[num] > max_freq:
                max_freq = freq[num]
                max_ele = num
            
            if max_freq * 2 > (index+1):
                prefix_dominant[index] = max_ele
        
        freq = {}
        suffix_dominant = [None] * nums_len
        max_ele = nums[-1]
        max_freq = 1
        for index in range(nums_len-1, -1, -1):
            num = nums[index]
            freq[num] = freq.get(num, 0) + 1
            if freq[num] > max_freq:
                max_freq = freq[num]
                max_ele = num
            
            if max_freq * 2 > (nums_len-index):
                suffix_dominant[index] = max_ele
        
        # print(prefix_dominant)
        # print(suffix_dominant)
        
        for index in range(nums_len-1):
            if prefix_dominant[index] == suffix_dominant[index+1]:
                return index
    
        return -1