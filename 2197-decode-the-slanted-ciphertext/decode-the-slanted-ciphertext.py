class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        encoded_text_length = len(encodedText)
        columns = encoded_text_length // rows
        original_text = ""
        for index in range(columns):
            original_text += encodedText[index]
            for row in range(1, rows):
                next_char_index = index + (columns+1) * row
                if next_char_index >= encoded_text_length: continue
                original_text += encodedText[next_char_index]
        return original_text.rstrip()
