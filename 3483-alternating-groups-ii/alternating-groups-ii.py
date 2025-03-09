class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        colors = colors + colors[:k]
        groups = 0
        start = 0

        for index, color in enumerate(colors[1:], start=1):
            if colors[index] == colors[index-1]:
                start = index-1
            else:
                if index - start < k:
                    continue
            
            if index - start == k:
                groups += 1
                start += 1
        
        return groups
