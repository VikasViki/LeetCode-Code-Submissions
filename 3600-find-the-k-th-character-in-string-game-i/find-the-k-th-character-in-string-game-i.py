next_char = {char: chr(ord(char)+1) for char in ascii_lowercase}
next_char['z'] = 'a'
curr_word = 'a'
while len(curr_word) < 500:
    new_word = ""
    for char in curr_word:
        new_word += next_char[char]
    curr_word = curr_word + new_word

class Solution:
    def kthCharacter(self, k: int) -> str:
        return curr_word[k-1]