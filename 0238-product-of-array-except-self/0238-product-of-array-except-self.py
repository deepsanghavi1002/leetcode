class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        ans[0] = 1
        prdt = 1
        for i in range(1, len(nums)):
            ans[i] = nums[i-1] * ans[i-1]
        for i in reversed(range(len(nums))):
            ans[i] = ans[i] * prdt
            prdt *= nums[i]
            
        return(ans)
            
            
        