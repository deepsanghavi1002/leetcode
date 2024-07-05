class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total = 0 
        valley = sys.maxsize
        peak = valley 
        
        
        diff = [prices[i+1] - prices[i] for i in range(len(prices) - 1)]
        print(diff)
        for i in range(len(prices)):
            if prices[i] < peak:
                total += peak - valley
                
                valley = prices[i]
                peak = valley
                
            else:
                peak = prices[i]
                
        total += peak - valley 
        
        ans = sum([i for i in diff if i>0])
        return ans