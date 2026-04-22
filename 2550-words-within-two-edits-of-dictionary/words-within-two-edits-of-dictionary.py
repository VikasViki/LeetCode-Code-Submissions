class Solution:

    def is_same_after_2_edits(self, query_word, dictionary_word):
        if len(query_word) != len(dictionary_word):
            return False
        edit = 0
        for query_word_char, dictionary_word_char in zip(query_word, dictionary_word):
            if query_word_char != dictionary_word_char:
                edit += 1
        return edit <= 2

    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        answer = []
        for query_word in queries:
            for dictionary_word in dictionary:
                if self.is_same_after_2_edits(query_word, dictionary_word):
                    answer.append(query_word)
                    break
        return answer
