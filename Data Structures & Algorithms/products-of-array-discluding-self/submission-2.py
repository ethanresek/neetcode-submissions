class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        result = []
        for i in range(len(nums)):
            excluded = nums[0 : i] + nums[i + 1 : len(nums)]
            prod = 1
            for num in excluded:
                prod *= num
            result.append(prod)
        
        return result
