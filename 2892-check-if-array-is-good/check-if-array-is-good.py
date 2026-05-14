class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums)-1
        nums_set = set(nums)
        if nums.count(n) != 2:
            return False

        for num in range(1, n+1):
            if num not in nums_set:
                return False
        
        return True
