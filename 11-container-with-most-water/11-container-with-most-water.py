class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        maxarea = 0
        while i < j:
            width = j - i 
            area = min(height[i], height[j]) * width
            maxarea = max(maxarea, area)
            
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
            
        return maxarea