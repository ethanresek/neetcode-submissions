class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        pre = [0] * len(nums)
        pre[0] = nums[0]
        for i in range(1, len(nums)):
            pre[i] = nums[i] * pre[i - 1]
        
        post = [0] * len(nums)
        post[len(nums) - 1] = nums[len(nums) - 1]
        for i in range(len(nums) - 2, -1, -1):
            post[i] = nums[i] * post[i + 1]

        products = []

        for i in range(len(nums)):
            
            total = 1

            if i > 0:
                total *= pre[i - 1]
            if i + 1 < len(nums):
                total *= post[i + 1]
            
            products.append(total)
        
        return products
