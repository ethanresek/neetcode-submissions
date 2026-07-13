class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        total = 1
        non_zero_total = 1
        zero_count = 0
        for n in nums:
            total *= n
            if n != 0:
                non_zero_total *= n
            else:
                zero_count += 1

        if zero_count > 1:
            return [0] * len(nums) 

        output = [total] * len(nums)

        for i in range(len(output)):
            if nums[i] == 0:
                output[i] = non_zero_total
            else:
                output[i] = output[i] // nums[i]
        
        return output