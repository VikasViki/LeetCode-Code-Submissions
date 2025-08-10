class TrieNode:
    def __init__(self, char):
        self.char = char
        self.children = {}
        self.is_word = False
        self.word_length = 0
    
    def __repr__(self):
        return f"char:{self.char} | children:{[char for char in self.children.keys()]} | is_word:{self.is_word} | word_length:{self.word_length}"

class Trie:
    def __init__(self):
        self.root = TrieNode("*")
    
    def add_words_to_trie(self, words):
        for word in words:
            self.add_word_to_trie(word)
    
    def add_word_to_trie(self, word):
        curr = self.root
        word_length = 1
        for char in word:
            if char not in curr.children.keys():
                char_node = TrieNode(char)
                char_node.word_length = word_length
                curr.children[char] = char_node

            curr = curr.children[char]
            word_length += 1
        curr.is_word = True
        # print(curr)
        # print(f"{word} added to trie. Length:{curr.word_length}. is_word:{curr.is_word}")
    
    def get_longest_word_in_trie(self, curr):
        longest_word = ""
        for char in curr.children.keys():
            child = curr.children[char]
            # print(curr.char, child)
            if child.is_word:
                continuous_word = char + self.get_longest_word_in_trie(child)
                if len(continuous_word) > len(longest_word):
                    longest_word = continuous_word
                elif len(continuous_word) == len(longest_word):
                    longest_word = min(longest_word, continuous_word)
        return longest_word


class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        trie.add_words_to_trie(words)
        longest_word = trie.get_longest_word_in_trie(trie.root)
        # print(f"Longest Word: {longest_word}")
        return longest_word