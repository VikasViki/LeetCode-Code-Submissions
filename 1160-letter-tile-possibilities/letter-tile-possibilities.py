from itertools import combinations, permutations

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        tiles_len = len(tiles)
        all_combinations = []
        for comb_len in range(1, tiles_len+1):
            for comb in combinations(tiles, comb_len):
                all_combinations.append(comb)
        
        sequences = set()
        for comb in all_combinations:
            for perm in permutations(comb):
                sequences.add("".join(perm))
        
        return len(sequences)
        