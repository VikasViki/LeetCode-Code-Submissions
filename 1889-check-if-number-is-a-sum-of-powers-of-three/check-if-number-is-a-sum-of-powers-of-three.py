class Solution:

    def __init__(self):
        self.values = []
        for power in range(20):
            value = 3 ** power
            if value > 10**7:
                break
            self.values.append(value)
        self.values_len = len(self.values)

    def check_subsequence_sum(self, index, n, subseq_sum):
        if subseq_sum == n:
            return True

        if index == self.values_len:
            return False

        memo_key = (index, subseq_sum)
        
        if memo_key in self.memo:
            return self.memo[memo_key]
        
        # Include curr value
        include = self.check_subsequence_sum(index+1, n, subseq_sum+self.values[index])

        # Exclude curr value
        exclude = self.check_subsequence_sum(index+1, n, subseq_sum)

        self.memo[memo_key] = include or exclude

        return self.memo[memo_key]


    def checkPowersOfThree(self, n: int) -> bool:
        self.memo = {}
        return self.check_subsequence_sum(0, n, 0)

    


        