class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        if (len(nums) == 1) or (len(nums) == 2 and nums[0] <= nums[1]):
            return 0
        small = min(nums)
        large = max(nums)
        
        small_index = nums.index(small)
        large_index = nums[::-1].index(large)
        print(small_index, large_index)
        
        if small_index>= len(nums) - large_index:
            return small_index + large_index -1
        return small_index+large_index