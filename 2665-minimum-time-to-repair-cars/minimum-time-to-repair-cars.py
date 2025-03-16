class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        min_rank, max_rank = ranks[0], ranks[0]

        for rank in ranks:
            min_rank = min(min_rank, rank)
            max_rank = max(max_rank, rank)
        
        freq = [0] * (max_rank + 1)
        for rank in ranks:
            freq[rank] += 1
        
        low = 1
        high = max_rank * cars * cars

        while low < high:
            mid = (low + high) // 2
            cars_repaired = 0

            for rank in range(1, max_rank+1):
                cars_repaired += freq[rank] * int(math.sqrt(mid // rank))
            
            if cars_repaired >= cars:
                high = mid
            else:
                low = mid + 1
        
        return low