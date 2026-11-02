class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        output = []
        for i in range(len(nums) - (k - 1)):
            j = i + k
            output.append(max(nums[i : j]))
        
        return output