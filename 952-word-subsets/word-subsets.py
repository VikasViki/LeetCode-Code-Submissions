class Solution:

    def get_char_freq(self, word):
        char_freq = {}
        for char in word:
            char_freq[char] = char_freq.get(char, 0) + 1
        return char_freq
    
    def is_universal_string(self, word, word2_freq):
        word_freq = self.get_char_freq(word)
        for char, count in word2_freq.items():
            char_count_in_word = word_freq.get(char, 0)
            if char_count_in_word < count:
                return False
        return True


    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:

        # Creating frequency dictionary consiting max frequeny in any single frequency
        words2_freq = {}
        for word in words2:
            word_freq = self.get_char_freq(word)
            for char, count in word_freq.items():
                words2_freq[char] = max(words2_freq.get(char, 0), count)
        
        universal_strings = []
        for word in words1:
            if self.is_universal_string(word, words2_freq):
                universal_strings.append(word)
        
        return universal_strings