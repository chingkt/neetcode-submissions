class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_left = [0] * len(height)
        max_right = [0] * len(height)

        for i in range(len(height)):
            if i == 0:
                max_left[i] = height[i]
            else:
                max_left[i] = max(height[i-1], max_left[i-1])

        for i in range(len(height)-1, -1, -1):
            if i == len(height) - 1:
                max_right[i] = height[i]
            else:
                max_right[i] = max(height[i+1], max_right[i+1])
        
        res = 0

        for i in range(len(height)):
            water_area = min(max_left[i], max_right[i]) - height[i]
            if water_area > 0:
                res += water_area
            print(i, max_left[i], max_right[i], res)
        return res
