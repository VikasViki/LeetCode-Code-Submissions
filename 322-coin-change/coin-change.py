class Solution:
    def coinChange(self, coins: List[int], total_amount: int) -> int:
        if total_amount == 0: return 0
        dp = [float('inf')] * (total_amount+1)

        for amount in range(total_amount+1):
            for coin in coins:

                if amount == coin:
                    dp[amount] = 1
                    break
                
                if coin <= amount:
                    dp[amount] = min(dp[amount], dp[amount-coin] + 1)
        
        return dp[total_amount] if dp[total_amount] != float('inf') else -1