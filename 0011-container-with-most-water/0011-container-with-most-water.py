class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0 
        right = len(height) - 1
        width = right - left
        area = 0
        while left < right:
            area = max(area, (right-left)* min(height[right], height[left]))
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
                
        return area