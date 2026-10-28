class Solution:
    def trap(self, height: List[int]) -> int:
        
        left_heights = [0] * len(height)
        left_heights[0] = height[0]
        for i in range(1, len(height)):
            left_heights[i] = max(left_heights[i - 1], height[i])
        
        right_heights = [0] * len(height)
        right_heights[len(height) - 1] = height[len(height) - 1]
        for i in range(len(height) - 2, -1, -1):
            right_heights[i] = max(right_heights[i + 1], height[i])
        
        total = 0
        for i in range(1, len(height) - 1):
            left_height = left_heights[i - 1]
            right_height = right_heights[i + 1]
            curr_height = height[i]
            if left_height > curr_height and right_height > curr_height:
                total += min(left_height, right_height) - curr_height
        
        return total
