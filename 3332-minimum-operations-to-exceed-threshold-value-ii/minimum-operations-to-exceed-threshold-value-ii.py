class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        min_heap = []
        for num in nums:
            heappush(min_heap, num)
        
        operations = 0
        while min_heap[0] < k:
            min1 = heappop(min_heap)
            min2 = heappop(min_heap)
            new_num = min(min1, min2) * 2 + max(min1, min2)
            heappush(min_heap, new_num)
            operations += 1
        
        return operations
