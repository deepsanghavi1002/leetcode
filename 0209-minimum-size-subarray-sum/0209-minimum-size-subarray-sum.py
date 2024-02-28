class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        j = 0
        total = 0
        res = len(nums)+1
        for j in range(len(nums)):
            
            total += nums[j]
            
            while i<len(nums) and total >= target:
                
                res = min(res, j-i+1)
                total -= nums[i]
                i+=1
                
        return res if res <= len(nums) else 0

            
            
                    
            