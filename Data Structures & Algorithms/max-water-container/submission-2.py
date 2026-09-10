class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        most = 0

        for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                area = min(heights[i], heights[j]) * abs(j - i)
                if area > most:
                    most = area
        
        return most