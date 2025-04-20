class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        freq = Counter(answers)
        min_rabbits = 0

        for key, count in freq.items():
            if key == 0:
                min_rabbits += count
                continue

            if key >= count:
                min_rabbits += (key+1)
                continue
            
            dividend = (count) // (key+1)
            remainder = (count) % (key+1)
            min_rabbits += (dividend) * (key+1)

            if remainder != 0:
                min_rabbits += (key+1)

        return min_rabbits