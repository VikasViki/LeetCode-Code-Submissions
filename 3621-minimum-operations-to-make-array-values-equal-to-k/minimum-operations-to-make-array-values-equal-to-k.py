class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        freq = Counter(nums)
        operations = 0
        for num, count in freq.items():
            if num < k:
                return -1
            elif num > k:
                operations += 1
        return operations