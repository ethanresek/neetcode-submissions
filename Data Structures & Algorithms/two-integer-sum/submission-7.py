class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        checked = {}

        for i, num in enumerate(nums):
            partner = target - num
            if partner in checked:
                return [checked[partner], i]

            checked[num] = i
        
        return []