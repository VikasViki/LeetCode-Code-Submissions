class Solution:

    def is_all_vowels_present(self, vowels):
        for char, count in vowels.items():
            if count <= 0:
                return False
        return True
    
    def get_substrings_count(self, word, k):
        start = 0
        index = 0
        word_len = len(word)
        constants_count = 0
        vowels = {'a': 0, 'e': 0, 'i': 0, 'o':0, 'u': 0}
        all_vowels = False
        substrings_count = 0

        while index < word_len:

            char = word[index]
            if char in vowels:
                vowels[char] += 1
            else:
                constants_count += 1
            
            all_vowels = self.is_all_vowels_present(vowels)
            while all_vowels and constants_count >= k:

                substrings_count += (word_len - index)
                char = word[start]
                if char in vowels:
                    vowels[char] -= 1
                else:
                    constants_count -= 1
                start += 1

                all_vowels = self.is_all_vowels_present(vowels)
        
            index += 1
        
        return substrings_count

    def countOfSubstrings(self, word: str, k: int) -> int:
        k_substrings_count = self.get_substrings_count(word, k)
        k_plus_1_substrings_count = self.get_substrings_count(word, k+1)

        return k_substrings_count - k_plus_1_substrings_count
        
            

                