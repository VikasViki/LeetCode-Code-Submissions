class Solution:

    def is_same_freq(self, s1_freq, s2_freq):
        for char in ascii_lowercase:
            if s1_freq.get(char, 0) != s2_freq.get(char, 0):
                return False
        return True

    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_freq = Counter(s1)
        s1_len = len(s1)
        s2_len = len(s2)

        if s1_len > s2_len:
            return False

        s2_freq = {}
        for index in range(s1_len):
            char = s2[index]
            s2_freq[char] = s2_freq.get(char, 0) + 1
        
        if self.is_same_freq(s1_freq, s2_freq):
            return True
        
        
        for index in range(s1_len, s2_len):
            char = s2[index]
            start_char = s2[index-s1_len]
            s2_freq[char] = s2_freq.get(char, 0) + 1
            s2_freq[start_char] -= 1

            if self.is_same_freq(s1_freq, s2_freq):
                return True
        
        return False
        

        



