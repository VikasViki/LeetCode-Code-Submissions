class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k == 1:
            return 0

        splits = []
        total_weights = len(weights)

        for index in range(1, total_weights):
            cost = weights[index] + weights[index-1]
            splits.append(cost)
        
        splits.sort()
        k -= 1
        max_score = sum(splits[-k:])
        min_score = sum(splits[:k])

        return max_score - min_score
