class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        nums_set = set(nums)

        for i, val in enumerate(nums[::-1]):
            partner = target - val
            if partner in nums_set:
                return [nums.index(partner), len(nums) - i - 1]
        
        return []