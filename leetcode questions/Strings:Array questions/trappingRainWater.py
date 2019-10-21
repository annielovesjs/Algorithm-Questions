class Solution(object):
    def trap(self, height):
        max_left = 0
        max_right = 0
        left = 0
        result = 0
        right = len(height) - 1
        
        while left < right:
            if height[left] < height[right]:
                if height[left] >= max_left:
                    max_left = height[left]
                else:
                    result += max_left - height[left]
                left+=1

            else:
                if max_right <= height[right]:
                    max_right = height[right]
                else:
                    result += max_right - height[right]
                right-=1
        return result
        