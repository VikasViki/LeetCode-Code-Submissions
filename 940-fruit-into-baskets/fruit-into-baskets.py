class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        freq = {}
        start = 0
        max_fruits = 0
        total_fruits = len(fruits)

        for index, fruit in enumerate(fruits):
            freq[fruit] = freq.get(fruit, 0) + 1

            while start < total_fruits and len(freq) > 2:
                fruit_to_remove = fruits[start]
                freq[fruit_to_remove] -= 1
                if freq[fruit_to_remove] == 0:
                    freq.pop(fruit_to_remove)
                start += 1

            max_fruits = max(max_fruits, index-start+1)
        
        return max_fruits
