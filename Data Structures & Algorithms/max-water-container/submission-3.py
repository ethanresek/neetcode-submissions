class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l = 0
        r = len(heights) - 1
        most = 0

        while l < r:
            area = (r - l) * min(heights[r], heights[l])
            if area > most:
                most = area
            
            if heights[r] > heights[l]:
                l += 1
            else:
                r -= 1

        return most