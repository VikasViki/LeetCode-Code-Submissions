class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        # Brute Force
        pairs_count = 0
        nums_len = len(nums)
        for i in range(nums_len):
            for j in range(i+1, nums_len):
                if (nums[i] == nums[j]) and (i*j)%k == 0:
                    pairs_count += 1
        return pairs_count