class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        curr_max = 0
        maxx = 0
        
        
        
        for i in range(len(prices) - 1):
            c = prices[i+1] - prices[i]                 
            curr_max = max(c, curr_max+c)
            maxx = max(maxx, curr_max)
            
        return maxx