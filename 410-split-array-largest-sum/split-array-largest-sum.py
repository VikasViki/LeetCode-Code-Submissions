class Solution:

    def is_valid_subarr_sum(self, nums, subarr_sum, k):
        splits = 1
        curr_sum = 0
        for num in nums:
            curr_sum += num
            if curr_sum > subarr_sum:
                splits += 1
                curr_sum = num
        # print(subarr_sum, splits)
        return splits <= k   

    def splitArray(self, nums: List[int], k: int) -> int:
        if k == len(nums):
            return max(nums)

        start = max(nums)
        end = sum(nums)
        while start < end:
            mid = (start + end) // 2
            if self.is_valid_subarr_sum(nums, mid, k):
                end = mid
            else:
                start = mid + 1
        return start