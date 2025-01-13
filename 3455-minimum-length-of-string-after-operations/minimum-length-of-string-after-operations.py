class Solution:
    def minimumLength(self, s: str) -> int:
        freq = Counter(s)
        min_length = 0
        
        for char, count in freq.items():
            if count % 2 == 0:
                min_length += 2
            else:
                min_length += 1

        return min_length