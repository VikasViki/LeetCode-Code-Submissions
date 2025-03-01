class Solution:
    def countArrays(self, original: List[int], bounds: List[List[int]]) -> int:
        curr_u, curr_v = bounds[0]
        length = len(original)
        count = curr_v - curr_u + 1

        for index in range(1, length):
            diff = original[index] - original[index-1]
            u, v = bounds[index]
            curr_u = max(curr_u+diff, u)
            curr_v = min(curr_v+diff, v)
            if curr_u > curr_v:
                return 0
            count = min(count, curr_v-curr_u+1)
        
        return count
            
