class Solution:

    def get_reverse_num(self, num: int) -> int:
        str_num = str(num)
        return int(str_num[::-1])

    def mirrorDistance(self, n: int) -> int:
        reverse_n = self.get_reverse_num(n)
        return abs(n - reverse_n)