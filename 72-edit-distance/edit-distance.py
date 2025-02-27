class Solution:

    def get_min_distance(self, word1, word2, word1_index, word2_index):

        if (word1_index, word2_index) in self.memo:
            return self.memo[(word1_index, word2_index)]

        if word1_index >= len(word1):
            return len(word2) - word2_index
        
        if word2_index >= len(word2):
            return len(word1) - word1_index
        
        if word1[word1_index] != word2[word2_index]:
            add_char = self.get_min_distance(word1, word2, word1_index, word2_index+1)
            delete_char = self.get_min_distance(word1, word2, word1_index+1, word2_index)
            replace_char = self.get_min_distance(word1, word2, word1_index+1, word2_index+1)
            self.memo[(word1_index, word2_index)] = 1 + min(add_char, delete_char, replace_char)

        else:
            replace_char = self.get_min_distance(word1, word2, word1_index+1, word2_index+1)
            self.memo[(word1_index, word2_index)] = replace_char
        
        return self.memo[(word1_index, word2_index)]
        

    def minDistance(self, word1: str, word2: str) -> int:
        self.memo = {}
        return self.get_min_distance(word1, word2, 0, 0)
        