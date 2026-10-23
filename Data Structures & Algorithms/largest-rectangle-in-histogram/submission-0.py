class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        max_area = 0
        for i, h in enumerate(heights):

            l = i
            r = i

            while l - 1 >= 0 and heights[l - 1] >= h:
                l -= 1
            while r + 1 < len(heights) and heights[r + 1] >= h:
                r += 1

            area = h * (r - l + 1)

            if area > max_area:
                max_area = area
        
        return max_area


