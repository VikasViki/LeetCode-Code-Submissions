
class Solution:

    def get_all_combinations(self, string, limit):
        if len(string) == limit:
            self.combinations.add(string)
            return
        
        for char in 'abc':
            if string and string[-1] == char: continue
            self.get_all_combinations(string+char, limit)


    def getHappyString(self, n: int, k: int) -> str:
        self.combinations = set()
        self.get_all_combinations("", n)
        if len(self.combinations) >= k:
            return sorted(self.combinations)[k-1]
        else:
            return ""