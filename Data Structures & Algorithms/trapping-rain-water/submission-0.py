class Solution:
    def trap(self, heights: List[int]) -> int:
        
        total_trapped = 0

        for pos, height in enumerate(heights):

            left_max = 0
            right_max = 0

            for left_pos, left_height in enumerate(heights[:pos]):
                if left_height > left_max:
                    left_max = left_height
            
            for right_pos, right_height in enumerate(heights[pos + 1:]):
                if right_height > right_max:
                    right_max = right_height

            if left_max > height and right_max > height:
                total_trapped += min(left_max, right_max) - height
        
        return total_trapped
        