class Solution:
    def decodeString(self, s: str) -> str:
        num = 0
        string = ""
        stack = []
        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            elif char.isalpha():
                string += char
            elif char == "[":
                stack.append(string)
                stack.append(num)
                string = ""
                num  = 0
            elif char == "]":
                prev_num = stack.pop()
                prev_string = stack.pop()
                string = prev_string + prev_num * string
        
        return string