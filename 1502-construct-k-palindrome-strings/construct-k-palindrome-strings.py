class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        s_len = len(s)
        if s_len == k:
            return True
        
        if s_len < k:
            return False
        
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1

        odds = 0
        for char, count in freq.items():
            if count % 2 != 0:
                odds += 1
        
        if odds > k:
            return False
        
        return True