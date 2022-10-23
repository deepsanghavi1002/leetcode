class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxReach = 0 
        i = 0
        target = len(nums)
        while(i<len(nums) and i<=maxReach):
            print(i)
            maxReach = max(i + nums[i], maxReach)
            i+=1

        if i == target:
            return True
        return False