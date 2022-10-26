class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        if min(coins) > amount:
            return -1
        
        dp = [0] + [float('inf')] * amount
        print(dp)
        
        for i in range(1,amount+1):
            
            for c in coins:
                if i -c < 0:
                    continue
                dp[i] = min(dp[i],dp[i-c]+1)
                
        print(dp)
        return dp[-1] if dp[-1] <= amount else -1