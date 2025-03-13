class Solution:

    def can_form_zero_array(self, nums, queries, k):
        nums_len = len(nums)
        total_sum = 0
        diff_array = [0] * (nums_len+1)

        for left, right, val in queries[:k]:
            diff_array[left] += val
            diff_array[right+1] -= val
        
        for index in range(nums_len):
            total_sum += diff_array[index]
            if total_sum < nums[index]:
                return False
        
        return True


    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        left, right = 0, len(queries)

        if not self.can_form_zero_array(nums, queries, right):
            return -1
        
        while left <= right:
            mid = (left + right) // 2
            if self.can_form_zero_array(nums, queries, mid):
                right = mid - 1
            else:
                left = mid + 1
        
        return left