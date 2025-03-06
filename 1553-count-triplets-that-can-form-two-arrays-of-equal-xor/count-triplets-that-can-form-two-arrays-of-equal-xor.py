class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        prefix_xor = [0] + arr[:]
        size = len(prefix_xor)
        for index in range(1, size):
            prefix_xor[index] ^= prefix_xor[index-1]
        
        count = 0
        for start in range(size):
            for end in range(start+1, size):
                if prefix_xor[start] == prefix_xor[end]:
                    count += (end - start - 1)
        
        return count
