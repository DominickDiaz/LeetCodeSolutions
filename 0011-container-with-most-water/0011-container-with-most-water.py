class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0 
        right = len(height) - 1
        x = 0
        y = 0 
        temp = 0
        maxWater = 0 
        
        
        while left != right: 
            x = right - left
            y = min(height[left], height[right])
            temp = x * y
            maxWater = max(temp, maxWater)
                
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            
        return maxWater
            
        