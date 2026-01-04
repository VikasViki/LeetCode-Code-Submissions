import math
def get_four_divisors_sum(num):
    divisor_sum = 0
    divisor_found = False
    limit = floor(sqrt(num))
    # print(num, limit)
    for divisor in range(2, limit+1):
        if num % divisor == 0:
            if divisor_found:
                return 0
            if divisor != (num // divisor):
                divisor_sum += divisor
                divisor_sum += (num // divisor)
                divisor_found = True
            else:
                return 0
    
    if divisor_found:
        return divisor_sum + 1 + num
    else:
        return 0

four_divisors_sum = {}
for num in range(2, 100001):
    divisors_sum = get_four_divisors_sum(num)
    if divisors_sum != 0:
        four_divisors_sum[num] = divisors_sum

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        # print(four_divisors_sum)
        sum_of_divisors = 0
        for num in nums:
            sum_of_divisors += four_divisors_sum.get(num, 0)
        return sum_of_divisors