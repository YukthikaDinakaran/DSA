class Solution(object):
    def maxArea(self, height):
        n = len(height)
        left = 0
        right = n-1 
        vol = 0
        while left < right:
            width = right - left 
            ht = min(height[left], height[right])
            area = width*ht
            vol = max(vol, area)

            if(height[left]< height[right]):
                left = left+1
            else:
                right = right -1 
        return vol
            
            


       