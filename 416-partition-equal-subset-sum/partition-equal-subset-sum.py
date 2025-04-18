class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        memo = {}

        def dfs(nums: Tuple[int], n: int, subset_sum: int) -> bool:
            # Base cases
            key = (n, subset_sum) 
            if key in memo:
                return memo[key]

            if subset_sum == 0:
                return True
            if n == 0 or subset_sum < 0:
                return False
            result = (dfs(nums, n - 1, subset_sum - nums[n - 1])
                    or dfs(nums, n - 1, subset_sum))

            memo[key] = result
            return result

        # find sum of array elements
        total_sum = sum(nums)

        # if total_sum is odd, it cannot be partitioned into equal sum subsets
        if total_sum % 2 != 0:
            return False

        subset_sum = total_sum // 2
        n = len(nums)
        return dfs(tuple(nums), n - 1, subset_sum)