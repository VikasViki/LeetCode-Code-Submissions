class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        xor_sum = 0
        for bit in derived:
            xor_sum = xor_sum ^ bit
        return xor_sum == 0