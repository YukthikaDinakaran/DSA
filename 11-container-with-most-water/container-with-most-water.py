class Solution(object):
    def maxArea(self, height):
        l = 0
        r = len(height) - 1
        max_area = 0

        while l < r:
            # width of container
            w = r - l

            # height of water (smaller line)
            h = min(height[l], height[r])

            # current area
            area = w * h
            max_area = max(max_area, area)

            # move the pointer with smaller height
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_area
