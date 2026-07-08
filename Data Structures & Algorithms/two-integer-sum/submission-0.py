class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        matching = set()

        for i in range(len(nums)):
            match = target - nums[i]
            if match in matching:
                return [nums.index(match), i]
            matching.add(nums[i])
        
        return None