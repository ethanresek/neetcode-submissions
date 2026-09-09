"""
Plan
create two arrays: prefix and suffix
for prefix
    prefill array with 1s length of nums
    input nums[0] at index 0
    multiply each value by the value before it
for suffix
    prefill array with 1s length of nums
    input nums[len(nums) - 1] at index len(prefix) - 1
    multiply each value by the value after it

loop through nums

    if in range:
        get the prefix value (current - 1) 
        get the suffix value (current + 1)

Multiply those together and append to output array
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix = [1] * len(nums)
        suffix = [1] * len(nums)

        prefix[0] = nums[0]
        suffix[len(suffix) - 1] = nums[len(nums) - 1]

        for i in range(1, len(prefix)):
            prefix[i] = nums[i] * prefix[i - 1]
        for i in range(len(suffix) - 2, 0, -1):
            suffix[i] = nums[i] * suffix[i + 1]

        result = []

        for i in range(len(nums)):

            pre = 1
            if i > 0:
                pre = prefix[i - 1]
            
            suf = 1
            if i < len(suffix) - 1:
                suf = suffix[i + 1]
        
            result.append(pre * suf)
        
        return result