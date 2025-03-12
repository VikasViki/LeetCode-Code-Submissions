class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        positive = 0
        negative = 0
        for num in nums:
            if num < 0:
                negative += 1
            elif num > 0:
                positive += 1
        
        return max(positive, negative)