class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product_of_digits = 1
        sum_of_digits = 0

        while n:
            rem = n % 10
            n = n // 10
            product_of_digits *= rem
            sum_of_digits += rem
        
        return product_of_digits - sum_of_digits