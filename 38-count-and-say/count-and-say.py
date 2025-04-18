class Solution:

    def get_compressed_string(self, string):
        compressed_string = ""
        prev_char = string[0]
        count = 0
        for char in string:
            if char == prev_char:
                count += 1
            else:
                compressed_string += str(count) + str(prev_char)
                count = 1
            prev_char = char
        compressed_string += str(count) + str(prev_char)
        return compressed_string

    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        string = self.countAndSay(n-1)
        rle = self.get_compressed_string(string)
        return rle
        
