class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        matching = {}

        for i in range(len(nums)):
            match = target - nums[i]
            if match in matching:
                return [matching[match], i]
            matching[nums[i]] = i
        
        return None