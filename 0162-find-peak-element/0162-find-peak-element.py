class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        return self.helper(0,len(nums)-1, nums)
    
    def helper(self, l, r, nums):
        if l==r:
            return l
        mid = (l+r) // 2
        if (nums[mid] < nums[mid+1]):
            return self.helper(mid+1, r, nums)
        return self.helper(l,mid, nums)
    
            