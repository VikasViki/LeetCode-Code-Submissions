class Solution:

    def is_allocation_possible(self, candies, max_candies, total_children):
        children = 0
        for candy in candies:
            children += (candy // max_candies)
        return children >= total_children


    def maximumCandies(self, candies: List[int], k: int) -> int:
        left = 1
        right = max(candies)
        
        while left <= right:
            mid = (left+right)//2

            if self.is_allocation_possible(candies, mid, k):
                left = mid + 1
            else:
                right = mid - 1
        
        return left - 1