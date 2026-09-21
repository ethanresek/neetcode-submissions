class Solution:
    def trap(self, height: List[int]) -> int:
        
        left_max = [height[0]] * len(height)
        right_max = [height[-1]] * len(height)

        for i in range(1, len(height)):
            left_max[i] = max(left_max[i - 1], height[i])
        for i in range(len(height) - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])
        
        total_trapped = 0

        for i, val in enumerate(height):

            if left_max[i] > val and right_max[i] > val:
                total_trapped += min(left_max[i], right_max[i]) - val

        return total_trapped