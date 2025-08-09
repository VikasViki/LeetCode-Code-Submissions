class Solution:
    
    def get_compressed_string(self, string: str) -> List[Tuple[str, int]]:
        compressed_string = []
        prev_char = string[0]
        count = 1
        for char in string[1:]:
            if char == prev_char:
                count += 1
            else:
                compressed_string.append((prev_char, count))
                prev_char = char
                count = 1
        compressed_string.append((prev_char, count))
        return compressed_string
    
    def is_stretchy_strings(self, compressed_s: List[Tuple[str, int]], compressed_word: List[Tuple[str, int]]) -> bool:
        print(compressed_s, compressed_word)
        compressed_s_len = len(compressed_s)
        compressed_word_len = len(compressed_word)
        if compressed_s_len != compressed_word_len:
            return False

        for index in range(compressed_word_len):
            s_char, s_count = compressed_s[index]
            word_char, word_count = compressed_word[index]
            if word_char != s_char:
                return False

            if word_count > s_count:
                return False
            
            elif word_count != s_count and s_count < 3:
                return False

        return True

    def expressiveWords(self, s: str, words: List[str]) -> int:
        compressed_s = self.get_compressed_string(s)
        stretchy_strings = 0

        for word in words:
            compressed_word = self.get_compressed_string(word)
            if self.is_stretchy_strings(compressed_s, compressed_word):
                stretchy_strings += 1
        
        return stretchy_strings
