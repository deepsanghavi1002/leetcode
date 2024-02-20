class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [0 for i in range(len(nums))]
        target = len(nums) - 1
        dp[0] = nums[0]
        if len(nums) in [0,1]:
            return True
        for i in range(1,len(nums)):
            if i > dp[i-1]:
                return False
            dp[i] = max(nums[i] + i, dp[i-1])
            #print(i,nums[i] + i, nums[i-1], dp)
            
        
        return True
  