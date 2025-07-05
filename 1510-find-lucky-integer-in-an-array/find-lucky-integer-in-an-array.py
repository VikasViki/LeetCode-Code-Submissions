class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = sorted(Counter(arr).items(), reverse=True)
        for val, count in freq:
            if val == count:
                return val
        return -1
        