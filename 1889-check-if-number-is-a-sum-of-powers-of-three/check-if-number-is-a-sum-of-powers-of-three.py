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
        if index == self.values_len:
            if subseq_sum == n:
                return True
            else:
                return False
        
        # Include curr value
        include = self.check_subsequence_sum(index+1, n, subseq_sum+self.values[index])

        # Exclude curr value
        exclude = self.check_subsequence_sum(index+1, n, subseq_sum)

        return include or exclude


    def checkPowersOfThree(self, n: int) -> bool:
        return self.check_subsequence_sum(0, n, 0)

    


        