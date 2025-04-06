class Solution:

    def set_union(self, set1, set2):
        return set1.union(set2)

    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        nums_len = len(nums)
        dp = {index:{num} for index,num in enumerate(nums)}

        for left_index in range(nums_len-1, -1, -1):
            left_num = nums[left_index]
            max_subset = {}
            for right_index in range(left_index+1, nums_len):
                right_num = nums[right_index]
                if right_num % left_num == 0:
                    curr_subset = dp[right_index]
                    if len(curr_subset) > len(max_subset):
                        max_subset = curr_subset
            dp[left_index] = self.set_union(dp[left_index], max_subset)

        largest_divisible_subset = {}
        max_subset_len = 0

        for index, subset in dp.items():
            curr_subset_len = len(subset)
            if curr_subset_len > max_subset_len:
                largest_divisible_subset = subset
                max_subset_len = curr_subset_len
        
        return list(largest_divisible_subset)