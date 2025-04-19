class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        black = set(map(tuple, coordinates))
        block_count = defaultdict(int)

        for x, y in black:
            for dx in [0, -1]:
                for dy in [0, -1]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m - 1 and 0 <= ny < n - 1:
                        block_count[(nx, ny)] += 1

        result = [0] * 5
        total_blocks = (m - 1) * (n - 1)

        for count in block_count.values():
            result[count] += 1

        result[0] = total_blocks - sum(result[1:])
        return result