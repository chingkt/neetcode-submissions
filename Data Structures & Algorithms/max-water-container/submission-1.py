class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # 1. depends on the distance
        # 2. depends on the min height
        # water = distance * min(height1, height2)
        left, right = 0, len(heights) - 1
        maxWater = 0

        while left < right:
            water = (right - left) * min(heights[left], heights[right])
            if water > maxWater:
                maxWater = water
            if heights[right] < heights[left]:
                right -= 1
            else:
                left += 1
        return maxWater
