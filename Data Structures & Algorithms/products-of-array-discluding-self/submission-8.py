class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        left = [0] * len(nums)
        left[0] = nums[0]

        for i in range(1, len(nums)):
            left[i] = nums[i] * left[i - 1]
        
        right = [0] * len(nums)
        right[len(right) - 1] = nums[len(nums) - 1]

        for i in range(len(nums) - 2, -1, -1):
            right[i] = nums[i] * right[i + 1]
        
        out = []

        for i in range(len(nums)):

            total = 1

            if i > 0:
                total *= left[i - 1]
            if i < len(nums) - 1:
                total *= right[i + 1]
            
            out.append(total)
        
        return out
            
