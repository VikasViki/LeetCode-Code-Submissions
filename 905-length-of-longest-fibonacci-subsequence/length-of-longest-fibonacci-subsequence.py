class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        nums_set = set(arr)
        max_len = 0
        n = len(arr)

        for first in range(n):
            for second in range(first+1, n):
                prev = arr[second]
                curr = arr[first] + arr[second]
                curr_len = 2

                while curr in nums_set:
                    prev, curr = curr, curr+prev
                    curr_len += 1
                    max_len = max(max_len, curr_len)
            
        return max_len