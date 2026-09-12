class Solution:
    def trap(self, height: List[int]) -> int:
        
        total_trapped = 0
        left_max = [height[0]] * len(height)
        right_max = [height[len(height) - 1]] * len(height)

        for i in range(1, len(left_max)):
            left_max[i] = max(height[i], left_max[i - 1])
        
        for i in range(len(right_max) - 2, -1, -1):
            right_max[i] = max(height[i], right_max[i + 1])

        for pos, val in enumerate(height):
            if left_max[pos] > val and right_max[pos] > val:
                total_trapped += min(left_max[pos], right_max[pos]) - val

        return total_trapped