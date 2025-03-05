class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes = sorted(envelopes, key = lambda x: (x[0], -x[1]))
        dp = []
        
        for width, height in envelopes:
            index = bisect_left(dp, height)
            dp_len = len(dp)
            if index == dp_len:
                dp.append(height)
            else:
                dp[index] = height
        
        return len(dp)
                    