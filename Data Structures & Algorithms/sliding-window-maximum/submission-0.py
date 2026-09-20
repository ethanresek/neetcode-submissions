class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        maxes = []

        for i in range(len(nums) - k + 1):
            maxes.append(max(nums[i : i + k]))
        
        return maxes