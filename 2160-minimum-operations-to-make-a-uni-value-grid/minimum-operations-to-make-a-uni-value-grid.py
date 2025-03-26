class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        remainder = grid[0][0] % x
        nums = []
        suffix_sum = 0
        for row in grid:
            for num in row:
                if num % x != remainder:
                    return -1
                nums.append(num)
                suffix_sum += num

        nums.sort()

        min_operations = float('inf')
        prefix_sum = 0
        nums_len = len(nums)

        for index, num in enumerate(nums):
            suffix_sum -= num
            left_operations = (num * index) - prefix_sum
            right_operations = suffix_sum - (num * (nums_len-index-1))
            total_operations = (left_operations + right_operations) // x
            min_operations = min(min_operations, total_operations)
            prefix_sum += num 
        
        return min_operations
