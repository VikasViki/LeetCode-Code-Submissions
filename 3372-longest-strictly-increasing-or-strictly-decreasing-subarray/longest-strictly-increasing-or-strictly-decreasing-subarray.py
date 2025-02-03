class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        longest_subarr = 0

        # strictly increasing
        stack = []
        for index, num in enumerate(nums):
            if stack and nums[stack[-1]] >= nums[index]:
                stack = []
            stack.append(index)
            longest_subarr = max(longest_subarr, len(stack))

        # Strictly decreasing
        stack = []
        for index, num in enumerate(nums):
            if stack and nums[stack[-1]] <= nums[index]:
                stack = []
            stack.append(index)
            longest_subarr = max(longest_subarr, len(stack))
        
        return longest_subarr