class Solution:

    def get_a_b_c_count(self, char, a, b, c, diff):
        if char == 'a':
            return (a+diff, b, c)
        elif char == 'b':
            return (a, b+diff, c)
        elif char == 'c':
            return (a, b, c+diff)

    def numberOfSubstrings(self, s: str) -> int:
        s_len = len(s)
        start = 0
        end = 0
        a = b = c = 0
        substrings_count = 0

        while end < s_len:
            a, b, c = self.get_a_b_c_count(s[end], a, b, c, 1)
            
            while start < end and a >= 1 and b >= 1 and c >= 1:
                substrings_count += s_len - end
                a, b, c = self.get_a_b_c_count(s[start], a, b, c, -1)
                start += 1
            
            end += 1
        
        return substrings_count