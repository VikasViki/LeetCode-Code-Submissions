class Solution:
    def is_symmetric(self, num):
        str_num = str(num)
        num_len = len(str_num)
        if num_len % 2 != 0:
            return False
        
        mid = num_len // 2
        left_sum = sum(int(digit) for digit in str_num[:mid])
        right_sum = sum(int(digit) for digit in str_num[mid:])

        return left_sum == right_sum 

    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for num in range(low, high+1):
            if self.is_symmetric(num):
                count += 1
        return count