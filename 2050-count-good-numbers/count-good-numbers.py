class Solution:

    def __init__(self):
        self.MOD = 10**9 + 7

    def mod_fast_pow(self, base, power):
        result = 1

        while power:
            if power % 2 == 1:
                result = ( result * base ) % self.MOD
            
            base = ((base % self.MOD) * (base % self.MOD)) % self.MOD
            power = power // 2
        
        return result

    def countGoodNumbers(self, n: int) -> int:
        even_digits = 5
        prime_digits = 4

        total_digits = n
        even_places = (total_digits + 1) // 2
        odd_places = total_digits - even_places

        even_places_permutations = self.mod_fast_pow(even_digits, even_places)
        odd_places_permutations  = self.mod_fast_pow(prime_digits, odd_places)

        good_numbers_count = ((even_places_permutations % self.MOD) * (odd_places_permutations % self.MOD)) % self.MOD

        return good_numbers_count

