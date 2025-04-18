class Solution:

    def __init__(self):
        self.rle = ["", "1"]
        self.build_rle(n=30)
    
    def get_compressed_string(self, string):
        compressed_string = ""
        count = 0
        prev_char = string[0]
        for char in string:
            if char == prev_char:
                count += 1
            else:
                compressed_string += str(count) + str(prev_char)
                count = 1
            prev_char = char
        
        compressed_string += str(count) + str(prev_char)
        return compressed_string

    
    def build_rle(self, n):
        for index in range(n-1):
            prev_string = self.rle[-1]
            compressed_string = self.get_compressed_string(prev_string)
            self.rle.append(compressed_string)

    def countAndSay(self, n: int) -> str:
        # print(len(self.rle))
        return self.rle[n]