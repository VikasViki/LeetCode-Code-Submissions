class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        for query in queries:
            left, right, step, multiple = query
            for index in range(left, right+1, step):
                nums[index] = (nums[index] * multiple) % 1000000007
        
        xor_result = 0
        for num in nums:
            xor_result ^= num
        
        return xor_result
