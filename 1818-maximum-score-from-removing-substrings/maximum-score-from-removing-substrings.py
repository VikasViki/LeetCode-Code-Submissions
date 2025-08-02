class Solution:

    def find_substring_count(self, string, substring):
        if not string:
            return 0, ""
            
        stack = [string[0]]
        substring_count = 0
        for char in string[1:]:
            if stack and stack[-1] + char == substring:
                    substring_count += 1
                    stack.pop()
            else:
                stack.append(char)
        
        return substring_count, "".join(stack)



    def maximumGain(self, s: str, x: int, y: int) -> int:
        # ab count
        ab_count, string = self.find_substring_count(s, 'ab')
        ba_count, string = self.find_substring_count(string, 'ba')
        score1 = ab_count * x + ba_count * y

        ba_count, string = self.find_substring_count(s, 'ba')
        ab_count, string = self.find_substring_count(string, 'ab')
        score2 = ba_count * y + ab_count * x

        return max(score1, score2)

