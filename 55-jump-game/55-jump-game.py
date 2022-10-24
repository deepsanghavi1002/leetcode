class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxReach = 0 
        i = 0
        target = len(nums)
        
        for i in range(len(nums)):
            
            maxReach = max(i + nums[i], maxReach)
            print(i, maxReach)
            if i >= maxReach:
                print("==",i,maxReach)
                break
        print("outside",maxReach,i)
        if i == len(nums) -1:
            return True
        return False