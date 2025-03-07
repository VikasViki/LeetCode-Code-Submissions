class Solution:

    def __init__(self):
        limit = ((10**6)+1)
        self.prime = [True] * limit
        self.prime[0] = False
        self.prime[1] = False
        factor = 2
        while factor < limit:
            if self.prime[factor]:
                for index in range(2*factor, limit, factor):
                    self.prime[index] = False
            factor += 1

    def closestPrimes(self, left: int, right: int) -> List[int]:
        ans = [-1, -1]
        num1 = num2 = -1
        ans_diff = float('inf')

        for num in range(left, right+1):
            if self.prime[num]:
                if num1 == -1:
                    num1 = num
                
                elif num2 == -1:
                    num2 = num
                    ans = [num1, num2]
                    ans_diff = num2 - num1
                  
                else:
                    num1 = num2
                    num2 = num
                    diff = num2 - num1
                    if diff < ans_diff:
                        ans = [num1, num2]
                        ans_diff = diff

        return ans if ans_diff != float('inf') else [-1, -1]
