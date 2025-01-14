class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        freq = {}
        prefix_commons = []
        common = 0
        
        for char_a, char_b in zip(A, B):
            freq[char_a] = freq.get(char_a, 0) + 1
            if freq[char_a] == 2:
                common += 1
            
            freq[char_b] = freq.get(char_b, 0) + 1
            if freq[char_b] == 2:
                common += 1
            
            prefix_commons.append(common)
        
        return prefix_commons
