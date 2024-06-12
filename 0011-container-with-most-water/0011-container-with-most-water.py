class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0 
        right = len(height) -1
        area = 0
        while left<right:
            width = right - left 
            area = max(width * min(height[left],height[right]), area)
            if height[left] >= height[right]:
                right -=1
            elif height[left] < height[right]:
                left += 1
            print(left,right, area)
        return area
                