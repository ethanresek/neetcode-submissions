class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = [1] * len(nums)
        prefix[0] = nums[0]
        suffix = [1] * len(nums)
        suffix[len(nums) - 1] = nums[len(nums) - 1]

        for i in range(1, len(nums)):
            prefix[i] = nums[i] * prefix[i - 1]
        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = nums[i] * suffix[i + 1]
        
        output = [0] * len(nums)

        for i in range(len(nums)):
            
            pre = 1
            suf = 1

            if i - 1 >= 0:
                pre = prefix[i - 1]
            if i + 1 < len(output):
                suf = suffix[i + 1]
            
            output[i] = pre * suf
            
        
        return output


