class Solution:

    def is_valid_divisor(self, divisor, nums, threshold):
        divisor_sum = 0
        for num in nums:
            divisor_sum += math.ceil(num/divisor)
        return divisor_sum <= threshold

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        start = 1
        end = max(nums)
        ans = 1

        while start <= end:
            mid = (start + end) // 2
            if self.is_valid_divisor(mid, nums, threshold):
                ans = mid
                end = mid - 1
            else:
                start = mid + 1
        
        return ans