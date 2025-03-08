class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        white_count = 0
        for index in range(k):
            if blocks[index] == "W":
                white_count += 1
            
        min_operations = white_count
        blocks_len = len(blocks)
        for index in range(k, blocks_len):
            if blocks[index] == "W":
                white_count += 1

            if blocks[index-k] == "W":
                white_count -= 1
            
            min_operations = min(min_operations, white_count)
        
        return min_operations