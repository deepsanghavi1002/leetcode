class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        diff = [prices[i+1] - prices[i] for i in range(len(prices) - 1)]
        curr_max = 0
        maxx = 0
        for c in diff:
            curr_max = max(c, curr_max+c)
            maxx = max(maxx, curr_max)
            
        return maxx