class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:

        total_workers = len(costs)

        first_candidates = []
        for index, cost in enumerate(costs[:candidates]):
            heappush(first_candidates, (cost, index))
        # print(first_candidates)

        last_candidates = []
        for index, cost in enumerate(costs[-candidates:], start=total_workers-candidates):
            heappush(last_candidates, (cost, index))
        
        # print(last_candidates)
        # Boundary
        first_group = candidates
        last_group = total_workers-candidates-1

        hired_workers = set()
        
        # print("group start", first_group, last_group)
        total_cost = 0
        for session in range(k):
            while first_candidates and first_candidates[0][1] in hired_workers:
                heappop(first_candidates)

            first_cost, first_index = first_candidates[0] if first_candidates else (float('inf'), None)
            
            while last_candidates and last_candidates[0][1] in hired_workers:
                heappop(last_candidates)

            last_cost, last_index = last_candidates[0] if last_candidates else (float('inf'), None)

            # print(f"first_cost:{first_cost} first_index:{first_index} first_group:{first_group}")
            # print(f"last_cost:{last_cost} last_index:{last_index} last_group:{last_group}")

            if first_cost <= last_cost:
                total_cost += first_cost
                hired_workers.add(first_index)
                heappop(first_candidates)
                
                if first_group < total_workers:
                    heappush(first_candidates, (costs[first_group], first_group))
                    first_group += 1
            
            else:
                total_cost += last_cost
                hired_workers.add(last_index)
                heappop(last_candidates)

                if last_group >= -total_workers:
                    heappush(last_candidates, (costs[last_group], last_group))
                    last_group -= 1
            
            # print(f"first_candidates:{first_candidates}, last_candidates:{last_candidates}")
        
        return total_cost
