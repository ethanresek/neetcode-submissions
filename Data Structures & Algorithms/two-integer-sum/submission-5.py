"""
Plan:
 - Convert nums into a set
 - Loop through each value in nums
    - if target - val in nums_set return both indices
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i, num in enumerate(nums):
            partner = target - num

            if partner in nums[:i] or partner in nums[i + 1:]:
                for j, num in enumerate(nums):
                    if j == i:
                        continue
                    if num == partner:
                        idx = j
                        break
                return [i, idx]
        
        return []