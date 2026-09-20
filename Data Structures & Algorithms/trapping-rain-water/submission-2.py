class Solution:
    def trap(self, height: List[int]) -> int:
        
        left_max = [0] * len(height)
        right_max = [0] * len(height)

        left_max[0] = height[0]
        right_max[len(height) - 1] = height[len(height) - 1]

        for i in range(1, len(height)):
            left_max[i] = max(height[i], left_max[i - 1])
        for i in range(len(height) - 2, -1, -1):
            right_max[i] = max(height[i], right_max[i + 1])

        total_trapped = 0

        for i, val in enumerate(height):
            if left_max[i] > val and right_max[i] > val:
                total_trapped += min(left_max[i], right_max[i]) - val
        
        return total_trapped