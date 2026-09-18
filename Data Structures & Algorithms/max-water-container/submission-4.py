class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        max_area = 0
        l = 0
        r = len(heights) - 1

        while l < r:
            curr_area = (r - l) * min(heights[l], heights[r])
            if curr_area > max_area:
                max_area = curr_area
            
            if heights[r] > heights[l]:
                l += 1
            else:
                r -= 1
        
        return max_area